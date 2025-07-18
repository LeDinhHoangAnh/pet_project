import React, { useEffect, useState } from 'react';
import dayjs from 'dayjs';
import 'dayjs/locale/vi';
import { getSeatStatusByShowtime } from '../api/seatApi';

const ShowTimeModal = ({ open, onClose, showtimes, movieTitle }) => {
  const [dates, setDates] = useState([]);
  const [selectedDate, setSelectedDate] = useState(dayjs().format('YYYY-MM-DD'));
  const [seatAvailability, setSeatAvailability] = useState({});
  const [hasFetched, setHasFetched] = useState(false);

  const showtimesOfDay = showtimes.filter(
    (show) => dayjs(show.start_time).format('YYYY-MM-DD') === selectedDate
  );

  useEffect(() => {
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
          const availableSeats = seatData.seats.filter(s => s.status === 'available').length;
          results[show.id] = availableSeats;
        } catch (error) {
          console.error('Lỗi khi tải ghế:', error);
          results[show.id] = 0;
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

  if (!open) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 z-50 flex items-center justify-center px-4">
      <div className="bg-white rounded-xl shadow-lg max-w-4xl w-full p-6 relative overflow-y-auto max-h-[90vh]">
        <div className="flex justify-between items-center mb-4 border-b pb-2">
          <h2 className="text-xl font-bold text-blue-700 flex items-center gap-2">
            🎬 Suất chiếu - {movieTitle}
          </h2>
          <button
            className="text-gray-600 hover:text-red-600 text-lg"
            onClick={onClose}
          >
            ✕
          </button>
        </div>

        {/* Thanh chọn ngày */}
        <div className="flex space-x-2 overflow-x-auto mb-6 border-b pb-2">
          {dates.map((date) => (
            <button
              key={date}
              onClick={() => {
                setSelectedDate(date);
                setHasFetched(false);
              }}
              className={`px-3 py-1 text-sm border-b-2 ${
                selectedDate === date
                  ? 'text-blue-600 border-blue-600 font-semibold'
                  : 'text-gray-500 border-transparent'
              }`}
            >
              {formatDateLabel(date)}
            </button>
          ))}
        </div>

        {/* Suất chiếu */}
        {showtimesOfDay.length === 0 ? (
          <p className="text-center text-gray-500">Không có suất chiếu trong ngày.</p>
        ) : (
          <div className="space-y-4">
            <div className="text-sm font-medium text-gray-600">2D Phụ đề</div>
            <div className="flex flex-wrap gap-3">
              {[...showtimesOfDay]
                .sort((a, b) => new Date(a.start_time) - new Date(b.start_time))
                .map((show) => (
                  <div
                    key={show.id}
                    className="p-3 border rounded-lg shadow-sm hover:bg-gray-100 cursor-pointer min-w-[80px] text-center"
                    onClick={() => {
                      const token = localStorage.getItem('token');
                      if (token) {
                        window.location.href = `/booking/${show.id}`;
                      } else {
                        localStorage.setItem('redirect_after_login', `/booking/${show.id}`);
                        window.location.href = '/login';
                      }
                    }}
                  >
                    <div className="font-semibold text-blue-700 text-lg">
                      {dayjs(show.start_time).format('HH:mm')}
                    </div>
                    <div className="text-xs text-gray-500 mt-1">
                      {seatAvailability[show.id] !== undefined
                        ? `${seatAvailability[show.id]} ghế trống`
                        : 'Đang tải...'}
                    </div>
                  </div>
                ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default ShowTimeModal;
