// src/api/bookingApi.js
import axios from 'axios';
import { getToken } from '../utils/auth';

const API_BASE = process.env.REACT_APP_API_BASE_URL;

export const createBooking = (bookingData) => {
  return axios.post(`${API_BASE}/api/bookings/`, bookingData, {
    headers: {
      Authorization: `Bearer ${getToken()}`,
    },
  });
};

export const getBookingHistory = async () => {
  return axios.get(`${API_BASE}/api/booking/history/`, {
    headers: {
      Authorization: `Bearer ${getToken()}`
    }
  });
};