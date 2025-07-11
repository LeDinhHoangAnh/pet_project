// src/pages/BookingPage.js
import React, { useEffect, useState, useMemo } from 'react';
import { useParams, Navigate } from 'react-router-dom';
import axios from 'axios';
import { getSeatStatusByShowtime } from '../api/seatApi';

const BookingPage = () => {
  const { showtimeId } = useParams();
  const [showtimeInfo, setShowtimeInfo] = useState(null);
  const [seats, setSeats] = useState([]);
  const [seatPrices, setSeatPrices] = useState({});
  const [selectedSeats, setSelectedSeats] = useState([]);
  const [loading, setLoading] = useState(true);
  const BASE_URL = process.env.REACT_APP_API_BASE_URL;

  // Kiểm tra login

  // Fetch tất cả
  useEffect(() => {
    const fetchAll = async () => {
      try {
        // 1. Chi tiết suất chiếu
        const det = await axios.get(`${BASE_URL}/api/showtimes/${showtimeId}/detail/`);
        setShowtimeInfo(det.data);

        // 2. Ghế trạng thái
        const st = await getSeatStatusByShowtime(showtimeId);
        setSeats(st.seats);

        // 3. Giá ghế
        const pr = await axios.get(`${BASE_URL}/api/seat-prices/${showtimeId}/`);
        const map = {};
        pr.data.forEach(item => {
          map[item.seat_type] = item.price;
        });
        setSeatPrices(map);

      } catch (e) {
        console.error(e);
      } finally {
        setLoading(false);
      }
    };
    fetchAll();
  }, [showtimeId]);

  // Toggle chọn ghế
  const toggleSeat = (seat) => {
    if (seat.status !== 'available') return;
    const exists = selectedSeats.find(s => s.id === seat.id);
    if (exists) {
      setSelectedSeats(prev => prev.filter(s => s.id !== seat.id));
    } else {
      if (selectedSeats.length >= 8) {
        alert('Chỉ được chọn tối đa 8 ghế!');
        return;
      }
      setSelectedSeats(prev => [...prev, seat]);
    }
  };

  // Tính tổng tiền
  const totalPrice = useMemo(() => {
    return selectedSeats.reduce((sum, seat) => {
      const price = seatPrices[String(seat.seat_type)] || 0;
      return sum + price;
    }, 0);
  }, [selectedSeats, seatPrices]);

  if (loading || !showtimeInfo) {
    return <p className="text-center mt-10">Đang tải dữ liệu...</p>;
  }

  // Nhóm ghế theo hàng
  const grouped = {};
  seats.forEach(seat => {
    const row = seat.seat_number.charAt(0);
    grouped[row] = grouped[row] || [];
    grouped[row].push(seat);
  });
  Object.values(grouped).forEach(arr =>
    arr.sort((a, b) => parseInt(a.seat_number.slice(1)) - parseInt(b.seat_number.slice(1)))
  );

  return (
    <div className="max-w-6xl mx-auto mt-10 px-4 grid grid-cols-1 md:grid-cols-3 gap-8">
      {/* Left: sơ đồ ghế */}
      <div className="md:col-span-2 bg-gray-100 p-4 rounded shadow">
        <h2 className="text-xl font-bold mb-4">Chọn ghế</h2>
        <div className="screen text-center mb-4 font-semibold py-1 bg-gray-300 rounded">MÀN HÌNH</div>

        {Object.keys(grouped).sort().map(row => (
          <div key={row} className="flex items-center mb-2">
            <span className="w-6 font-semibold">{row}</span>
            <div className="flex flex-wrap">
              {grouped[row].map(seat => {
                const isBooked = seat.status !== 'available';
                const isSelected = selectedSeats.find(s => s.id === seat.id);
                const style = isBooked
                  ? 'bg-gray-400 text-white cursor-not-allowed'
                  : isSelected
                    ? 'bg-blue-600 text-white'
                    : 'bg-white hover:bg-blue-100';
                const price = seatPrices[seat.seat_type] || 0;
                return (
                  <button
                    key={seat.id}
                    disabled={isBooked}
                    onClick={() => toggleSeat(seat)}
                    className={`m-1 px-3 py-2 text-sm border rounded ${style}`}
                    title={`Ghế ${seat.seat_number} — ${price.toLocaleString()} đ`}
                  >
                    <div>{seat.seat_number}</div>
                  </button>
                );
              })}
            </div>
          </div>
        ))}

        <div className="mt-4 flex gap-4 text-sm">
          <div><span className="inline-block w-4 h-4 bg-white border rounded mr-1"></span> Ghế trống</div>
          <div><span className="inline-block w-4 h-4 bg-blue-600 mr-1"></span> Ghế chọn</div>
          <div><span className="inline-block w-4 h-4 bg-gray-400 mr-1"></span> Ghế đã bán</div>
        </div>
      </div>

      {/* Right: thông tin đặt vé */}
      <div className="bg-white p-4 rounded shadow">
        <h3 className="text-xl font-semibold mb-4">Thông tin đặt vé</h3>
        <img
          src={`${BASE_URL}${showtimeInfo.movie.movie_poster_url}`}
          alt={showtimeInfo.movie.title}
          className="w-full h-48 object-cover rounded mb-4"
        />
        <p><strong>Tên phim:</strong> {showtimeInfo.movie.title}</p>
        <p><strong>Thể loại:</strong> {showtimeInfo.movie.genres.join(', ')}</p>
        <p><strong>Thời lượng:</strong> {showtimeInfo.movie.duration} phút</p>
        <p><strong>Ngày chiếu:</strong> {new Date(showtimeInfo.start_time).toLocaleDateString()}</p>
        <p><strong>Giờ chiếu:</strong> {new Date(showtimeInfo.start_time).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</p>
        <p><strong>Phòng chiếu:</strong> {showtimeInfo.room.room_name}</p>
        <div className="mt-4">
          <p><strong>Ghế đã chọn:</strong> {selectedSeats.map(s => s.seat_number).join(', ') || 'Chưa chọn'}</p>
          <p className="mt-2 font-bold"><strong>Tổng tiền:</strong> {totalPrice.toLocaleString()} đ</p>
        </div>
        <button
          className="mt-6 w-full bg-green-600 text-white py-2 rounded hover:bg-green-700 transition"
          disabled={selectedSeats.length === 0}
        >
          Xác nhận đặt vé
        </button>
      </div>
    </div>
  );
};

export default BookingPage;
