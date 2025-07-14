// src/pages/BookingPage.js
import React, { useEffect, useState, useMemo } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import { getSeatStatusByShowtime } from '../api/seatApi';
import ServiceSelector from './ServiceSelector';
import CheckoutPage from './CheckoutPage';

const BookingPage = () => {
  const { showtimeId } = useParams();
  const [showtimeInfo, setShowtimeInfo] = useState(null);
  const [seats, setSeats] = useState([]);
  const [seatPrices, setSeatPrices] = useState({});
  const [selectedSeats, setSelectedSeats] = useState([]);
  const [selectedServices, setSelectedServices] = useState([]);
  const [services, setServices] = useState([]);
  const [quantities, setQuantities] = useState({});
  const [loading, setLoading] = useState(true);
  const [step, setStep] = useState('select-seat'); // 'select-seat' | 'select-service' | 'checkout'
  const BASE_URL = process.env.REACT_APP_API_BASE_URL;

  const formatDateDMY = (isoDate) => {
    const d = new Date(isoDate);
    return `${String(d.getDate()).padStart(2, '0')}-${String(d.getMonth() + 1).padStart(2, '0')}-${d.getFullYear()}`;
  };

  useEffect(() => {
    const fetchAll = async () => {
      try {
        const det = await axios.get(`${BASE_URL}/api/showtimes/${showtimeId}/detail/`);
        setShowtimeInfo(det.data);

        const st = await getSeatStatusByShowtime(showtimeId);
        setSeats(st.seats);

        const pr = await axios.get(`${BASE_URL}/api/seat-prices/${showtimeId}/`);
        const map = {};
        pr.data.forEach(item => {
          map[item.seat_type_name] = item.price;
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

  const totalSeatPrice = useMemo(() => {
    return selectedSeats.reduce((sum, seat) => {
      const price = seatPrices[String(seat.seat_type_name)] || 0;
      return sum + price;
    }, 0);
  }, [selectedSeats, seatPrices]);

  if (loading || !showtimeInfo) {
    return <p className="text-center mt-10">Đang tải dữ liệu...</p>;
  }

  const grouped = {};
  seats.forEach(seat => {
    const row = seat.seat_number.charAt(0);
    grouped[row] = grouped[row] || [];
    grouped[row].push(seat);
  });
  Object.values(grouped).forEach(arr =>
    arr.sort((a, b) => parseInt(a.seat_number.slice(1)) - parseInt(b.seat_number.slice(1)))
  );

  // Điều hướng bước tiếp theo
  const handleNext = () => {
    if (step === 'select-seat') {
      setStep('select-service');
    } else if (step === 'select-service') {
      const selected = services
        .filter(s => (quantities[s.id] || 0) > 0)
        .map(s => ({ ...s, quantity: quantities[s.id] }));
      setSelectedServices(selected);
      setStep('checkout');
    }
  };

  const handleBack = () => {
    if (step === 'select-service') setStep('select-seat');
    else if (step === 'checkout') setStep('select-service');
  };

  return (
    <div className="max-w-7xl mx-auto mt-10 px-4 grid grid-cols-1 md:grid-cols-3 gap-8">
      {step === 'select-seat' && (
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
                  const price = seatPrices[String(seat.seat_type_name)] || 0;
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
          <div className="mt-4">
            <p><strong>Ghế đã chọn:</strong> {selectedSeats.map(s => s.seat_number).join(', ') || 'Chưa chọn'}</p>
            <p className="mt-2 font-bold"><strong>Tổng tiền:</strong> {totalSeatPrice.toLocaleString()} đ</p>
          </div>
        </div>
      )}

      {step === 'select-service' && (
        <ServiceSelector
          totalSeatPrice={totalSeatPrice}
          services={services}
          setServices={setServices}
          quantities={quantities}
          setQuantities={setQuantities}
        />
      )}

      {step === 'checkout' && (
        <CheckoutPage
          user={{ name: 'Nguyễn Văn A', email: 'a@gmail.com', phone: '0901234567' }}
          selectedSeats={selectedSeats}
          selectedServices={selectedServices}
          totalSeatPrice={totalSeatPrice}
        />
      )}

      {/* Right Panel */}
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
        <p><strong>Ngày chiếu:</strong> {formatDateDMY(showtimeInfo.start_time)}</p>
        <p><strong>Giờ chiếu:</strong> {new Date(showtimeInfo.start_time).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', hour12: false })}</p>
        <p><strong>Phòng chiếu:</strong> {showtimeInfo.room.room_name}</p>
        <div className="mt-4">
          <p><strong>Ghế đã chọn:</strong> {selectedSeats.map(s => s.seat_number).join(', ') || 'Chưa chọn'}</p>
        </div>

        {/* Action Buttons */}
        <div className="mt-6 w-full">
          <div className="flex gap-2">
          {step !== 'select-seat' && (
            <button
              onClick={handleBack}
              className="w-full bg-gray-500 text-white py-2 rounded hover:bg-gray-600 transition"
            >
              Quay lại
            </button>
          )}
          {step !== 'checkout' && (
            <button
              onClick={handleNext}
              className="w-full bg-green-600 text-white py-2 rounded hover:bg-green-700 transition"
              disabled={step === 'select-seat' && selectedSeats.length === 0}
            >
              Tiếp tục
            </button>
          )}
          {step === 'checkout' && (
            <button
              onClick={() => alert('Tiến hành thanh toán...')}
              className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700 transition"
            >
              Thanh toán
            </button>
          )}
          </div>
        </div>
      </div>
    </div>
  );
};


export default BookingPage;
