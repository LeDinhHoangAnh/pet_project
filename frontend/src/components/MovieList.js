import React, { useEffect, useState } from 'react';
import { getAllMovies } from '../api/movieApi';

const MovieList = () => {
  const [movies, setMovies] = useState([]);
  const BASE_URL = process.env.REACT_APP_API_BASE_URL;
  useEffect(() => {
    const fetch = async () => {
      const data = await getAllMovies();
      setMovies(data);
    };
    fetch();
  }, []);

  if (!movies.length) return <p className="text-center">Đang tải phim...</p>;

  return (
    <div className="container mx-auto px-4">
      <h2 className="text-2xl font-bold mb-4">📽️ Phim đang chiếu</h2>
      <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
        {movies.map((movie) => (
          <div key={movie.id} className="border shadow rounded overflow-hidden hover:shadow-lg">
              <img
              src={`${BASE_URL}${movie.movie_poster_url}`}
              alt={movie.title}
              className="rounded-md w-full h-64 object-cover"
            />
            <div className="p-3">
              <h3 className="text-lg font-semibold">{movie.title}</h3>
              <p className="text-sm text-gray-600">Thời lượng: {movie.duration} phút</p>
              <a href={`/movies/${movie.id}`} className="text-blue-500 text-sm hover:underline">
                Xem chi tiết
              </a>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default MovieList;
