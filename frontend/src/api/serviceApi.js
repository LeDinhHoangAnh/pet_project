import axios from 'axios';

const API_BASE = process.env.REACT_APP_API_BASE_URL;

export const getAllServices = async () => {
  const res = await axios.get(`${API_BASE}/api/services/`);
  return res.data;
};
