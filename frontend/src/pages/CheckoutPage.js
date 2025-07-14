// src/pages/CheckoutPage.js
import React from 'react';

const CheckoutPage = ({ user, selectedSeats, selectedServices, totalSeatPrice }) => {
  const totalServicePrice = selectedServices.reduce(
    (sum, s) => sum + s.quantity * s.service_price,
    0
  );
  const total = totalSeatPrice + totalServicePrice;

  return (
    <div className="md:col-span-2 bg-gray-100 p-4 rounded shadow">
      <h2 className="text-xl font-bold mb-4">Xác nhận thông tin</h2>

      <div className="mb-4">
        <p><strong>Tên:</strong> {user.name}</p>
        <p><strong>Email:</strong> {user.email}</p>
        <p><strong>SĐT:</strong> {user.phone}</p>
      </div>

      <div className="mb-4">
        <p><strong>Ghế đã chọn:</strong> {selectedSeats.map(s => s.seat_number).join(', ')}</p>
        <p><strong>Tiền vé:</strong> {totalSeatPrice.toLocaleString()} đ</p>
      </div>

      <div className="mb-4">
        <p className="font-semibold mb-1">Dịch vụ:</p>
        {selectedServices.length === 0 ? (
          <p>Không chọn dịch vụ nào</p>
        ) : (
          <ul>
            {selectedServices.map(s => (
              <li key={s.id}>
                {s.service_name} × {s.quantity} = {(s.service_price * s.quantity).toLocaleString()} đ
              </li>
            ))}
          </ul>
        )}
      </div>

      <p className="text-lg font-bold mt-4">Tổng cộng: {total.toLocaleString()} đ</p>
    </div>
  );
};

export default CheckoutPage;
