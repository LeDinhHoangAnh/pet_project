// pages/BookingHistoryPage.jsx
import React, { useEffect, useState } from 'react';
import { getBookingHistory } from '../api/bookingApi';
import { fetchBookingDetail } from '../api/bookingDetailApi';
import moment from 'moment';

const BookingHistoryPage = () => {
  const [bookings, setBookings] = useState([]);
  const [bookingDetails, setBookingDetails] = useState([]);

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
  const [bookingDetail, setBookingDetail] = useState(null);

  const handleViewDetail = async (bookingId) => {
  try {
    const res = await fetchBookingDetail(bookingId);
    setSelectedBooking(bookingId);
    setBookingDetail(res.data);
  } catch (error) {
    console.log("bbookingId", bookingId)
    console.error("Lỗi khi lấy chi tiết booking:", error);
  }
};


  return (
  <div className="max-w-7xl mx-auto mt-10 px-4">
    <h2 className="text-2xl font-bold mb-6">📜 Lịch sử đặt vé</h2>

    <div className="overflow-x-auto">
      <table className="min-w-full border border-gray-300 text-sm text-left">
        <thead className="bg-gray-100 text-gray-700 font-semibold">
          <tr>
            <th className="px-4 py-3 border">🎬 Phim</th>
            <th className="px-4 py-3 border">🕓 Thời gian</th>
            <th className="px-4 py-3 border">📍 Rạp / Phòng</th>
            <th className="px-4 py-3 border">💺 Ghế</th>
            <th className="px-4 py-3 border">💰 Tổng tiền</th>
            <th className="px-4 py-3 border">📅 Ngày đặt</th>
            <th className="px-4 py-3 border">🔍 Chi tiết</th>
          </tr>
        </thead>
        <tbody>
          {bookings.map(booking => (
            <tr key={booking.id} className="hover:bg-gray-50 transition">
              <td className="px-4 py-2 border">{booking.showtime.movie_title}</td>
              <td className="px-4 py-2 border">
               {moment(booking.showtime.start_time).format('DD/MM/YYYY HH:mm')}
              </td>
              <td className="px-4 py-2 border">
               {booking.showtime.room_name}
              </td>
              <td className="px-4 py-2 border">{booking.seats.join(', ')}</td>
              <td className="px-4 py-2 border">{booking.total_price.toLocaleString()} đ</td>
              <td className="px-4 py-2 border">
                {moment(booking.create_at).format('DD/MM/YYYY HH:mm')}
              </td>
              <td className="px-4 py-2 border">
             
                <button
                  className="text-blue-600 hover:underline"
                  onClick={() => handleViewDetail(booking.id)}
                >
                  Xem
                </button>
                {booking.is_new && <span className="bg-green-500 text-white text-xs px-2 py-1 rounded ml-5">Mới</span>}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>

    {/* Modal xem chi tiết */}
    {selectedBooking && (
      <div className="fixed inset-0 bg-black bg-opacity-40 flex items-center justify-center z-50">
        <div className="bg-white p-6 rounded shadow max-w-3xl w-full relative">
          <button
            className="absolute top-2 right-2 text-red-500 text-lg"
            onClick={() => setSelectedBooking(null)}
          >
            ✕
          </button>

          <h3 className="text-xl font-bold mb-4">Thông tin chi tiết</h3>

          {/* Bảng Ghế */}
          <div className="mb-4">
            <h4 className="font-semibold mb-2">Danh sách ghế</h4>
            <div className="overflow-x-auto">
              <table className="w-full text-sm border border-gray-300">
                <thead className="bg-gray-100">
                  <tr>
                    <th className="py-2 px-3 border">Số ghế</th>
                    <th className="py-2 px-3 border">Loại</th>
                    <th className="py-2 px-3 border">Giá</th>
                  </tr>
                </thead>
                <tbody>
                  {bookingDetail.seats?.map((seat, index) => (
                    <tr key={index}>
                      <td className="py-1 px-3 border text-center">{seat.seat_number}</td>
                      <td className="py-1 px-3 border text-center">{seat.seat_type}</td>
                      <td className="py-1 px-3 border text-right">
                        {seat.price?.toLocaleString()} đ
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
            <div className="text-right mt-2 font-semibold">
              Tổng tiền ghế: {bookingDetail.total_seat_price?.toLocaleString() || '0'} đ
            </div>
          </div>

          {/* Bảng Dịch Vụ */}
          <div className="mb-4">
            <h4 className="font-semibold mb-2">Dịch vụ kèm theo</h4>
            {bookingDetail.services && bookingDetail.services.length > 0 ? (
              <div className="overflow-x-auto">
                <table className="w-full text-sm border border-gray-300">
                  <thead className="bg-gray-100">
                    <tr>
                      <th className="py-2 px-3 border">Tên dịch vụ</th>
                      <th className="py-2 px-3 border">Số lượng</th>
                      <th className="py-2 px-3 border">Đơn giá</th>
                      <th className="py-2 px-3 border">Thành tiền</th>
                    </tr>
                  </thead>
                  <tbody>
                    {bookingDetail.services.map((service, index) => (
                      <tr key={index}>
                        <td className="py-1 px-3 border text-center">{service.service_name}</td>
                        <td className="py-1 px-3 border text-center">{service.quantity}</td>
                        <td className="py-1 px-3 border text-right">
                          {service.unit_price?.toLocaleString()} đ
                        </td>
                        <td className="py-1 px-3 border text-right">
                          {service.total_price?.toLocaleString()} đ
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            ) : (
              <p className="text-sm italic text-gray-500">Không có dịch vụ.</p>
            )}
            <div className="text-right mt-2 font-semibold">
              Tổng tiền dịch vụ: {bookingDetail.total_service_price?.toLocaleString() || '0'} đ
            </div>
          </div>

          {/* Tổng tiền */}
          <div className="text-right text-lg font-bold mt-4">
            Tổng cộng: {bookingDetail.total_price?.toLocaleString() || '0'} đ
          </div>
        </div>
      </div>
    )}


  </div>
  );
};

export default BookingHistoryPage;
