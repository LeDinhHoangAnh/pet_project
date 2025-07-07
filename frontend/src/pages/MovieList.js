import React, { useEffect, useState } from 'react';
import { getAllMovies } from '../api/movieApi';

const MovieList = () => {
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    getAllMovies()
      .then(res => setMovies(res.data))
      .catch(err => console.error('Lỗi tải danh sách phim:', err));
  }, []);

  return (
    <div>
      <h2>🎬 Danh sách phim</h2>
      <ul>
        {movies.map(movie => (
          <li key={movie.id}>
            <strong>{movie.title}</strong> ({movie.release_date})
          </li>
        ))}
      </ul>
    </div>
  );
};

export default MovieList;
