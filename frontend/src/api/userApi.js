import axios from 'axios';
import { getToken } from '../utils/auth';

const API_BASE = process.env.REACT_APP_API_BASE_URL;

export const getProfile = () => {
  const token = localStorage.getItem('token');
  return axios.get(`${API_BASE}/api/user/profile/`, {
    headers: { Authorization: `Bearer ${token}` }
  });
};

export const updateProfile = async (data) => {
  const token = getToken();
  return axios.put(`${API_BASE}/api/user/profile/`, data, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
};