import axiosInstance from './axiosConfig';

export const getProfile = () =>
  axiosInstance.get('/api/user/profile/');

export const updateProfile = data =>
  axiosInstance.put('/api/user/profile/', data);
