import React, { useState, useEffect } from 'react';
import dayjs from 'dayjs';
import 'dayjs/locale/vi';
import { getSeatStatusByShowtime } from '../api/seatApi';
import { fetchAllShowtimesGroupedByMovie } from '../api/showtimeApi';
import TicketModal from '../components/TicketModal';
import TrailerModal from '../components/TrailerModal';
import { getAllMovies, getGenresByMovie } from '../api/movieApi';

dayjs.locale('vi');

const MovieSchedulePage = () => {
  const [dates, setDates] = useState([]);
  const [selectedDate, setSelectedDate] = useState(dayjs().format('YYYY-MM-DD'));
  const [moviesByDate, setMoviesByDate] = useState({});
  const [seatAvailability, setSeatAvailability] = useState({});
  const [selectedShowtime, setSelectedShowtime] = useState(null);
  const [movies, setMovies] = useState([]);
  const [trailerInfo, setTrailerInfo] = useState({ url: '', title: '' });
  const [movieGenres, setMovieGenres] = useState({});

  useEffect(() => {
      const fetch = async () => {
        const data = await getAllMovies();
        setMovies(data);
  
        const genresMap = {};
        for (const movie of data) {
          const genres = await getGenresByMovie(movie.id);
          genresMap[movie.id] = genres.map(g => g.genre_name).join(', ');
        }
        setMovieGenres(genresMap);
      };
      fetch();
  }, []);
  
  useEffect(() => {
    const days = Array.from({ length: 7 }, (_, i) =>
      dayjs().add(i, 'day').format('YYYY-MM-DD')
    );
    setDates(days);
  }, []);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const rawData = await fetchAllShowtimesGroupedByMovie();
        const groupedByDate = {}; 
        for (const item of rawData) {
          const { date, movies } = item;
          groupedByDate[date] = movies;
        }
        setMoviesByDate(groupedByDate);
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
  
  const openTrailer = (url, title) => {
    setTrailerInfo({ url, title });
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
        {!moviesByDate[selectedDate] || moviesByDate[selectedDate].length === 0 ? (
          <p>Không có lịch chiếu ngày này.</p>
        ) : (
        moviesByDate[selectedDate].map((movie, idx) => (
          <div key={idx} className="mb-10">
            <div className="flex flex-col md:flex-row gap-6 p-4 bg-white rounded-xl shadow-lg">
              
              {/* Poster phim */}
              <div
                className="relative group w-full md:w-64 h-80 overflow-hidden rounded-lg shadow-md cursor-pointer"
                title={movie.title}
                onClick={() => openTrailer(movie.trailer_url, movie.title)}
              >
                <img
                  src={`${process.env.REACT_APP_API_BASE_URL}${movie.movie_poster_url}`}
                  alt={movie.title}
                  className="object-cover w-full h-full transition-transform duration-300 group-hover:scale-105"
                />
                <div className="absolute inset-0 flex items-center justify-center bg-black bg-opacity-40 opacity-0 group-hover:opacity-100 transition">
                  <span className="text-white text-5xl">⏵</span>
                </div>
              </div>

              {/* Thông tin phim */}
              <div className="flex-1">
                <a
                  href={`/movies/${movie.movie_id}`}
                  className="text-2xl font-bold text-gray-800 hover:underline"
                >
                  {movie.title}
                </a>
                
                {/* Thể loại và thời lượng */}
                <p className="text-gray-600 mt-1 flex items-center gap-2">
                  <span>🎬 {movie.genre}</span>
                  <span>⏱️ {movie.duration} phút</span>
                </p>

                {/* Loại chiếu */}
                <div className="mt-3 inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-50 text-blue-600 text-sm font-medium">
                  🕶️ 2D Phụ đề
                </div>

                {/* Suất chiếu */}
                <div className="mt-4">
                  <div className="text-gray-700 font-semibold mb-2">🕒 Suất chiếu:</div>
                  <div className="flex flex-wrap gap-3">
                    {[...movie.showtimes]
                      .sort((a, b) => new Date(a.start_time) - new Date(b.start_time))
                      .map((show) => (
                        <div
                          key={show.id}
                          onClick={() => handleShowtimeClick({ ...show, movie })}
                          className="px-4 py-2 border rounded-lg shadow-sm cursor-pointer hover:bg-blue-100 hover:border-blue-400 transition"
                        >
                          <div className="font-medium text-gray-800">
                            {dayjs(show.start_time).format('HH:mm')}
                          </div>
                          <div className="text-xs text-gray-500">
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

            {/* Trailer Modal */}
            {trailerInfo.url && (
              <TrailerModal
                trailerUrl={trailerInfo.url}
                movieTitle={trailerInfo.title}
                onClose={() => setTrailerInfo({ url: '', title: '' })}
              />
            )}
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
