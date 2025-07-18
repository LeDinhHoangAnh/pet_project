import React, { useEffect, useState, useRef } from 'react';
import { getAllMovies, getGenresByMovie, getShowtimesByMovie } from '../api/movieApi';
import TrailerModal from './TrailerModal';
import ShowTimeModal from './ShowTimeModal'; // Import modal hiển thị suất chiếu

const MovieList = () => {
  const [movies, setMovies] = useState([]);
  const [trailerInfo, setTrailerInfo] = useState({ url: '', title: '' });
  const [movieGenres, setMovieGenres] = useState({});
  const [showtimeModal, setShowtimeModal] = useState({ open: false, showtimes: [], movieTitle: '' });
  const hasFetched = useRef(false);
  const BASE_URL = process.env.REACT_APP_API_BASE_URL;

  useEffect(() => {
    const fetch = async () => {
      if (hasFetched.current) return; // ✅ chỉ gọi 1 lần
      hasFetched.current = true;

      const data = await getAllMovies();
      setMovies(data);

      const genresResults = await Promise.all(
        data.map(movie => getGenresByMovie(movie.id))
      );

      const genresMap = {};
      data.forEach((movie, index) => {
        genresMap[movie.id] = genresResults[index]
          .map(g => g.genre_name)
          .join(', ');
      });

      setMovieGenres(genresMap);
    };

    fetch();
  }, []);
  


  const openTrailer = (url, title) => {
    setTrailerInfo({ url, title });
  };

  const openShowtimeModal = async (movieId, movieTitle) => {
    const showtimeData = await getShowtimesByMovie(movieId);
    setShowtimeModal({
      open: true,
      showtimes: showtimeData,
      movieTitle: movieTitle
    });
  };

  if (!movies.length) return <p className="text-center">Đang tải phim...</p>;

  return (
    <div className="container mx-auto px-4 mt-10 mb-10">
      <div className="grid grid-cols-2 md:grid-cols-4 gap-6 mt-10 mb-20">
        {movies.map((movie) => (
          <div key={movie.id} className="border shadow rounded overflow-hidden hover:shadow-lg">
            <div
              className="relative group cursor-pointer"
              title={movie.title}
              onClick={() => openTrailer(movie.trailer_url, movie.title)}
            >
              <img
                src={`${BASE_URL}${movie.movie_poster_url}`}
                alt={movie.title}
                className="rounded-md w-full h-64 object-cover"
              />
              <div className="absolute inset-0 flex items-center justify-center bg-black bg-opacity-40 opacity-0 group-hover:opacity-100 transition">
                <span className="text-white text-4xl">⏵</span>
              </div>
            </div>

            <div className="p-3">
              <h3 className="text-lg font-semibold">
                <a
                  href={`/movies/${movie.id}`}
                  className="text-blue-500 hover:underline"
                >
                  {movie.title}
                </a>
              </h3>
              <p className="text-sm text-gray-600">Thời lượng: {movie.duration} phút</p>
              <p className="text-sm text-gray-600 italic">Thể loại: {movieGenres[movie.id] || 'Đang cập nhật...'}</p>
            </div>
            <button
              onClick={() => openShowtimeModal(movie.id, movie.title)}
              className="mt-2 bg-blue-600 text-white text-sm px-4 py-2 rounded hover:bg-blue-700 transition"
            >
              🎟️ Mua vé
            </button>
          </div>
        ))}
      </div>

      {trailerInfo.url && (
        <TrailerModal
          trailerUrl={trailerInfo.url}
          movieTitle={trailerInfo.title}
          onClose={() => setTrailerInfo({ url: '', title: '' })}
        />
      )}

      {showtimeModal.open && (
        <ShowTimeModal
          open={true} 
          showtimes={showtimeModal.showtimes}
          movieTitle={showtimeModal.movieTitle}
          onClose={() => setShowtimeModal({ open: false, showtimes: [], movieTitle: '' })}
        />
      )}
    </div>
  );
};

export default MovieList;
