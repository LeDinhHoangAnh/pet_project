import React, { useState, useEffect } from 'react';
import dayjs from 'dayjs';
import 'dayjs/locale/vi';
import TicketModal from '../components/TicketModal';
import { getSeatStatusByShowtime } from '../api/seatApi'; 

const ShowtimeList = ({ showtimes, movieTitle }) => {
  const [dates, setDates] = useState([]);
  const [selectedDate, setSelectedDate] = useState(dayjs().format('YYYY-MM-DD'));
  const [selectedShowtime, setSelectedShowtime] = useState(null);
  const [seatAvailability, setSeatAvailability] = useState({});
  const [hasFetched, setHasFetched] = useState(false);
  const handleShowtimeClick = (showtime) => {
    setSelectedShowtime(showtime);
  };
    const showtimesOfDay = showtimes.filter((show) =>
    dayjs(show.start_time).format('YYYY-MM-DD') === selectedDate
  );

  useEffect(() => {
    // Tạo danh sách 7 ngày từ hôm nay
    const days = Array.from({ length: 7 }, (_, i) =>
      dayjs().add(i, 'day').format('YYYY-MM-DD')
    );
    setDates(days);
  }, []);

    useEffect(() => {
    const fetchAllSeatAvailability = async () => {
      const results = {};
      for (const show of showtimesOfDay) {
        try {
          const seatData = await getSeatStatusByShowtime(show.id);
          const availableSeats = seatData.seats.filter(
            (s) => s.status === 'available'
          ).length;
          results[show.id] = availableSeats;
        } catch (error) {
          console.error('Lỗi khi tải số lượng ghế:', error);
          results[show.id] = 0; // fallback
        }
      }
      setSeatAvailability(results);
      setHasFetched(true);

    };

    if (showtimesOfDay.length > 0 && !hasFetched) {
      fetchAllSeatAvailability();
    }
  }, [showtimesOfDay]);


  const formatDateLabel = (date) => {
    const d = dayjs(date);
    return `${d.format('DD')}/07 - ${d.format('dd').toUpperCase()}`;
  };


  return (
    <div className="mt-10">
      {/* Thanh chọn ngày */}
      <div className="flex space-x-4 overflow-x-auto border-b mb-6">
        {dates.map((date) => (
          <button
            key={date}
            onClick={() => setSelectedDate(date)}
            className={`px-4 py-2 text-sm border-b-2 ${
              selectedDate === date
                ? 'text-blue-600 border-blue-600 font-bold'
                : 'text-gray-600 border-transparent'
            }`}
          >
            {formatDateLabel(date)}
          </button>
        ))}
      </div>

      {/* Suất chiếu trong ngày */}
      {showtimesOfDay.length === 0 ? (
        <p>Không có suất chiếu trong ngày.</p>
      ) : (
        <div className="space-y-4">
          <div className="text-lg font-semibold">2D Phụ đề</div>
          <div className="flex flex-wrap gap-4">
            {[...showtimesOfDay]
              .sort((a, b) => new Date(a.start_time) - new Date(b.start_time))
              .map((show) => (
                <div
                  key={show.id}
                  className="border p-4 rounded shadow-sm cursor-pointer hover:bg-gray-100"
                  onClick={() => handleShowtimeClick(show)}
                >
                  <div className="font-medium text-md">
                    {dayjs(show.start_time).format('HH:mm')}
                  </div>
                  <div className="text-xs text-gray-600">
                    {seatAvailability[show.id] !== undefined
                      ? `${seatAvailability[show.id]} ghế trống`
                      : 'Đang tải...'}
                  </div>
                </div>
              ))}
          </div>
        </div>
      )}
       <TicketModal
        show={!!selectedShowtime}
        showtime={{ ...selectedShowtime, movie: { title: movieTitle } }}
        onClose={() => setSelectedShowtime(null)}
      />

    </div>
  );
};

export default ShowtimeList;
