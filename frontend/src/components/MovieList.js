import React, { useEffect, useState } from 'react';
import { getAllMovies, getGenresByMovie } from '../api/movieApi';
import TrailerModal from './TrailerModal';


const MovieList = () => {
  const [movies, setMovies] = useState([]);
  const [trailerInfo, setTrailerInfo] = useState({ url: '', title: '' });
  const BASE_URL = process.env.REACT_APP_API_BASE_URL;
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

  const openTrailer = (url, title) => {
    setTrailerInfo({ url, title });
  };

  if (!movies.length) return <p className="text-center">Đang tải phim...</p>;

  return (
    <div className="container mx-auto px-4 mt-10 mb-10">
      <div className="grid grid-cols-2 md:grid-cols-4 gap-6 mt-10 mb-20">
        {movies.map((movie) => (
          <div key={movie.id} className="border shadow rounded overflow-hidden hover:shadow-lg">
            {/* CHỈ gắn sự kiện click vào ảnh */}
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

            {/* Tiêu đề là link sang trang chi tiết */}
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
              onClick={() => window.location.href = `/booking/${movie.id}`}
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

    </div>
  );
};

export default MovieList;
