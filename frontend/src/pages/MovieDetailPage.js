import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getMovieById, getShowtimesByMovie } from '../api/movieApi';
import MovieDetail from '../components/MovieDetail';

const MovieDetailPage = () => {
  const { id } = useParams();
  const [movie, setMovie] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      const movieData = await getMovieById(id);
      setMovie(movieData);
    };
    fetchData();
  }, [id]);

  if (!movie) return <p className="text-center">Đang tải chi tiết phim...</p>;

  return (
    <>
      <div className='mt-10'>
        <MovieDetail movie={movie} />
      </div>
    </>
  );
};

export default MovieDetailPage;
