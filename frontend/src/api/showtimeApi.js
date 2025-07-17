import axios from 'axios';

const BASE_URL = process.env.REACT_APP_API_BASE_URL;

export const fetchAllShowtimesGroupedByMovie = async () => {
  const res = await axios.get(`${BASE_URL}/api/showtimes/by-date/`);
  return res.data;
};
