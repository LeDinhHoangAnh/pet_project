// src/services/authService.js
import axios from 'axios';

const API_BASE = process.env.REACT_APP_API_BASE_URL + '/api/auth';

export const register = async (userData) => {
  return axios.post(`${API_BASE}/register/`, userData);
};

export const login = async (credentials) => {
  return axios.post(`${API_BASE}/login/`, credentials);
};
