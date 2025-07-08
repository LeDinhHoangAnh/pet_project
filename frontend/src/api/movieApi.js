// src/api/movieApi.js
import axios from 'axios';

const API_BASE = `${process.env.REACT_APP_API_BASE_URL}/api/movies/`;

export const getAllMovies = async () => {
  const res = await axios.get(API_BASE);
  return res.data;
};
