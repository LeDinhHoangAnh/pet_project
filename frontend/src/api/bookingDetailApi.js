import axios from 'axios';
import { getToken } from '../utils/auth';
const API_BASE = process.env.REACT_APP_API_BASE_URL;

export const fetchBookingDetail = async (bookingId) => {
  return axios.get(`${API_BASE}/api/bookings/${bookingId}/details/`, {
    headers: {
      Authorization: `Bearer ${getToken()}`
    }
  });
};

