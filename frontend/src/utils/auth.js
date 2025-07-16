import { jwtDecode } from 'jwt-decode';

export const saveToken = (token) => {
  localStorage.setItem('token', token);
  try {
    const decoded = jwtDecode(token);
    localStorage.setItem('user', JSON.stringify(decoded));
  } catch (err) {
    console.error("Lỗi giải mã JWT:", err);
  }
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

export const isLoggedIn = () => !!localStorage.getItem('token');

export const getCurrentUser = () => {
  const userStr = localStorage.getItem('user');
  return userStr ? JSON.parse(userStr) : null;
};

