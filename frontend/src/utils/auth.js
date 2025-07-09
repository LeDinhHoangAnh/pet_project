// src/utils/auth.js
import { jwtDecode } from 'jwt-decode';


export const saveToken = (token) => {
  localStorage.setItem('token', token);
};

export const getToken = () => {
  return localStorage.getItem('token');
};

export const decodeToken = () => {
  const token = getToken();
  if (!token) return null;
  return jwtDecode(token);
};

export const logout = () => {
  localStorage.removeItem('token');
};
