import axios from 'axios';

const BASE_URL = process.env.REACT_APP_API_BASE_URL;

export const getSeatStatusByShowtime = async (showtimeId) => {
  const res = await axios.get(`${BASE_URL}/api/showtimes/${showtimeId}/seat_status/`);
  return res.data;
};
