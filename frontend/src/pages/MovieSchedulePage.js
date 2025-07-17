import React, { useState, useEffect } from 'react';
import dayjs from 'dayjs';
import 'dayjs/locale/vi';
import { getSeatStatusByShowtime } from '../api/seatApi';
import { fetchAllShowtimesGroupedByMovie } from '../api/showtimeApi';
import TicketModal from '../components/TicketModal';

dayjs.locale('vi');

const MovieSchedulePage = () => {
  const [dates, setDates] = useState([]);
  const [selectedDate, setSelectedDate] = useState(dayjs().format('YYYY-MM-DD'));
  const [moviesByDate, setMoviesByDate] = useState({});
  const [seatAvailability, setSeatAvailability] = useState({});
  const [selectedShowtime, setSelectedShowtime] = useState(null);

  useEffect(() => {
    const days = Array.from({ length: 7 }, (_, i) =>
      dayjs().add(i, 'day').format('YYYY-MM-DD')
    );
    setDates(days);
  }, []);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const allData = await fetchAllShowtimesGroupedByMovie(); // Giả định API trả về dạng: { '2025-07-17': [{ movie, showtimes: [...] }], ... }
        setMoviesByDate(allData);
      } catch (error) {
        console.error('Lỗi khi tải lịch chiếu:', error);
      }
    };
    fetchData();
  }, []);

  useEffect(() => {
    const fetchSeats = async () => {
      const movieList = moviesByDate[selectedDate] || [];
      const results = {};

      for (const movie of movieList) {
        for (const show of movie.showtimes) {
          try {
            const data = await getSeatStatusByShowtime(show.id);
            const available = data.seats.filter(s => s.status === 'available').length;
            results[show.id] = available;
          } catch {
            results[show.id] = 0;
          }
        }
      }
      setSeatAvailability(results);
    };

    if (moviesByDate[selectedDate]) {
      fetchSeats();
    }
  }, [selectedDate, moviesByDate]);

  const formatDateLabel = (date) => {
    const d = dayjs(date);
    return `${d.format('DD')}/${d.format('MM')} - ${d.format('dd').toUpperCase()}`;
  };

  const handleShowtimeClick = (show) => {
    setSelectedShowtime(show);
  };
  
  return (
    
    <div className="p-6">
      {/* Thanh chọn ngày */}
      <div className="flex space-x-4 overflow-x-auto border-b mb-6">
        {dates.map((date) => (
          <button
            key={date}
            onClick={() => setSelectedDate(date)}
            className={`px-4 py-2 text-sm border-b-2 whitespace-nowrap ${
              selectedDate === date
                ? 'text-blue-600 border-blue-600 font-bold'
                : 'text-gray-600 border-transparent'
            }`}
          >
            {formatDateLabel(date)}
          </button>
        ))}
      </div>

      {/* Danh sách phim */}
      {(moviesByDate[selectedDate] || []).length === 0 ? (
        <p>Không có lịch chiếu ngày này.</p>
      ) : (
        moviesByDate[selectedDate].map((movie, idx) => (
          <div key={idx} className="mb-8">
            <div className="flex gap-4">
              <img
                src={movie.movie_poster_url}
                alt={movie.title}
                className="w-36 h-52 object-cover rounded"
              />
              <div>
                <h2 className="text-xl font-bold">{movie.title}</h2>
                <p className="text-sm text-gray-500">{movie.genre} • {movie.duration} phút</p>
                <div className="mt-2 text-sm font-medium">2D Phụ đề</div>
                <div className="flex flex-wrap gap-3 mt-2">
                  {[...movie.showtimes]
                    .sort((a, b) => new Date(a.start_time) - new Date(b.start_time))
                    .map((show) => (
                      <div
                        key={show.showtime_id}
                        onClick={() => handleShowtimeClick({ ...show, movie })}
                        className="px-3 py-1 border rounded shadow-sm cursor-pointer hover:bg-gray-100"
                      >
                        <div>{dayjs(show.start_time).format('HH:mm')}</div>
                        <div className="text-xs text-gray-600">
                          {seatAvailability[show.id] !== undefined
                            ? `${seatAvailability[show.id]} ghế trống`
                            : 'Đang tải...'}
                        </div>
                      </div>
                    ))}
                </div>
              </div>
            </div>
          </div>
        ))
      )}

      {/* Modal chọn vé */}
      <TicketModal
        show={!!selectedShowtime}
        showtime={selectedShowtime}
        onClose={() => setSelectedShowtime(null)}
      />
    </div>
  );
};

export default MovieSchedulePage;
