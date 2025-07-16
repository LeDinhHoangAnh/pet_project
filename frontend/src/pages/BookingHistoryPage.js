// pages/BookingHistoryPage.jsx
import React, { useEffect, useState } from 'react';
import { getBookingHistory } from '../api/bookingApi';
import moment from 'moment';

const BookingHistoryPage = () => {
  const [bookings, setBookings] = useState([]);

  useEffect(() => {
    const fetch = async () => {
      try {
        const res = await getBookingHistory();
        setBookings(res.data);
      } catch (e) {
        console.error('Lỗi lấy dữ liệu lịch sử:', e);
      }
    };
    fetch();
  }, []);

  const [selectedBooking, setSelectedBooking] = useState(null);

  return (
    <div className="max-w-4xl mx-auto mt-8 p-4 bg-white rounded shadow">
      <h2 className="text-2xl font-bold mb-4">📜 Lịch sử đặt vé</h2>
      {bookings.map(booking => (
        <div
          key={booking.id}
          className="border p-4 rounded mb-4 hover:bg-gray-50 transition cursor-pointer"
        >
          <div className="flex justify-between items-center">
            <div>
              <p><strong>🎬 Phim:</strong> {booking.showtime.movie_title}</p>
              <p><strong>🕓 Thời gian:</strong> {booking.showtime.show_date} - {booking.showtime.start_time}</p>
              <p><strong>📍 Phòng:</strong> {booking.showtime.room_name} - {booking.showtime.cinema_name}</p>
              <p><strong>💺 Ghế:</strong> {booking.seats.join(', ')}</p>
              <p><strong>💰 Tổng tiền:</strong> {booking.total_price.toLocaleString()} đ</p>
            </div>
            <div className="text-right">
              {booking.is_new && <span className="bg-green-500 text-white text-xs px-2 py-1 rounded">Mới</span>}
              <button
                className="text-blue-600 hover:underline mt-2 block"
                onClick={() => setSelectedBooking(booking)}
              >
                Xem chi tiết
              </button>
            </div>
          </div>
        </div>
      ))}

      {/* Modal xem chi tiết */}
      {selectedBooking && (
        <div className="fixed inset-0 bg-black bg-opacity-40 flex items-center justify-center z-50">
          <div className="bg-white p-6 rounded shadow max-w-lg w-full relative">
            <button className="absolute top-2 right-2 text-red-500" onClick={() => setSelectedBooking(null)}>✕</button>
            <h3 className="text-xl font-bold mb-4">Thông tin chi tiết</h3>
            <p><strong>Phim:</strong> {selectedBooking.showtime.movie_title}</p>
            <p><strong>Thời gian:</strong> {selectedBooking.showtime.show_date} - {selectedBooking.showtime.start_time}</p>
            <p><strong>Phòng:</strong> {selectedBooking.showtime.room_name}</p>
            <p><strong>Rạp:</strong> {selectedBooking.showtime.cinema_name}</p>
            <p><strong>Thời lượng:</strong> {selectedBooking.showtime.duration} phút</p>
            <p><strong>Ghế:</strong> {selectedBooking.seats.join(', ')}</p>
            <p><strong>Giá:</strong> {selectedBooking.total_price.toLocaleString()} đ</p>
            <p><strong>Ngày đặt:</strong> {moment(selectedBooking.create_at).format('DD/MM/YYYY HH:mm')}</p>
          </div>
        </div>
      )}
    </div>
  );
};

export default BookingHistoryPage;
