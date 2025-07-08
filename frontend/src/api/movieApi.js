// src/api/movieApi.js
import axios from 'axios';

const API_BASE = 'http://localhost:8000/api/movies/';

export const getAllMovies = async () => {
  const res = await axios.get(API_BASE);
  return res.data;
};
