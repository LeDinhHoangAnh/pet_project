import axios from 'axios';

const API_BASE = process.env.REACT_APP_API_BASE_URL;

export const getAllMovies = async () => {
  const res = await axios.get(`${API_BASE}/api/movies/`);
  return res.data;
};

export const getMovieById = async (id) => {
  const res = await axios.get(`${API_BASE}/api/movies/${id}/`);
  return res.data;
};

export const getShowtimesByMovie = async (movieId) => {
  const res = await axios.get(`${API_BASE}/api/movies/${movieId}/showtimes/`);
  return res.data;
};
