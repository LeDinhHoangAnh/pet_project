import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getMovieById, getShowtimesByMovie } from '../api/movieApi';
import ShowtimeList from '../components/ShowTime';

const MovieDetailPage = () => {
  const { id } = useParams();
  const [movie, setMovie] = useState(null);
  const [showtimes, setShowtimes] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const movieData = await getMovieById(id);
      setMovie(movieData);

       const showtimeData = await getShowtimesByMovie(id);
       setShowtimes(showtimeData);
    };
    fetchData();
  }, [id]);

  if (!movie) return <p className="text-center">Đang tải chi tiết phim...</p>;

  const youtubeId = movie.trailer_url?.split('v=')[1]?.split('&')[0];

  return (
    <>
      <div className="container mx-auto px-4 py-8 mt-5">
        {/* Thông tin phim */}
        <div className="flex flex-col md:flex-row gap-6 mb-8 mt-5">
          <img
            src={`${process.env.REACT_APP_API_BASE_URL}${movie.movie_poster_url}`}
            alt={movie.title}
            className="rounded-md w-[300px] h-[450px] object-cover object-center shadow"
          />
          <div className="flex-1">
            <h1 className="text-3xl font-bold mb-2">{movie.title}</h1>
            <p className="mb-4">{movie.description}</p>
            <ul className="text-sm space-y-1">
              <li><strong>Thể loại:</strong> {movie.genre || 'Đang cập nhật'}</li>
              <li><strong>Thời lượng:</strong> {movie.duration} phút</li>
              <li><strong>Ngôn ngữ:</strong> {movie.language || 'Tiếng Việt'}</li>
              <li><strong>Ngày khởi chiếu:</strong> {movie.release_date}</li>
              <li><strong>Đạo diễn:</strong> {movie.director || 'Chưa rõ'}</li>
              <li><strong>Diễn viên:</strong> {movie.cast || 'Đang cập nhật'}</li>
            </ul>
          </div>
        </div>

      </div>
      <div className="ml-6">
      <ShowtimeList showtimes={showtimes} />

      </div>
      {youtubeId && (
      <div className="w-screen bg-yellow-300 py-10 mt-20 flex flex-col items-center justify-center min-h-[1000px]">
        <h2 className="text-3xl font-bold text-black mb-6">🎬 Trailer phim: {movie.title}</h2>
        <div className="w-[90%] max-w-6xl h-[70%] aspect-video rounded-xl overflow-hidden shadow-2xl">
          <iframe
            src={`https://www.youtube.com/embed/${youtubeId}`}
            title={`Trailer ${movie.title}`}
            width="100%"
            height="100%"
            frameBorder="0"
            allowFullScreen
            className="rounded-xl"
          />
        </div>
      </div>
    )}
    </>
  );
};

export default MovieDetailPage;
