import React, { useEffect, useState } from 'react';

const CheckoutPage = ({ user,selectedSeats, selectedServices, totalSeatPrice }) => {
  const totalServicePrice = selectedServices.reduce(
    (sum, s) => sum + s.quantity * s.service_price,
    0
  );

  const total = totalSeatPrice + totalServicePrice;

  return (
    <div className="md:col-span-2 bg-white p-6 rounded shadow-md space-y-6">
      {/* 1. Thông tin người dùng */}
      <section>
        <h3 className="text-lg font-semibold mb-2">👤 Thông tin người dùng</h3>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div><strong>Họ tên:</strong> {user.name}</div>
          <div><strong>Email:</strong> {user.email}</div>
          <div><strong>Số ĐT:</strong> {user.phone}</div>
        </div>
      </section>

      {/* 2. Thông tin ghế */}
      <section>
        <h3 className="text-lg font-semibold mb-2">🎟 Ghế đã chọn</h3>
        <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
          <div><strong>Ghế:</strong> {selectedSeats.map(s => s.seat_number).join(', ')}</div>
          <div><strong>Tổng tiền vé:</strong> {totalSeatPrice.toLocaleString()} đ</div>
        </div>
      </section>

      {/* 3. Dịch vụ đi kèm */}
      <section>
        <h3 className="text-lg font-semibold mb-2">🍿 Dịch vụ đã chọn</h3>
        {selectedServices.length === 0 ? (
          <p>Không có dịch vụ nào</p>
        ) : (
          <ul className="list-disc pl-5 space-y-1">
            {selectedServices.map((s) => (
              <li key={s.id}>
                {s.service_name} × {s.quantity} = {(s.service_price * s.quantity).toLocaleString()} đ
              </li>
            ))}
          </ul>
        )}
      </section>

      {/* 4. Tổng tiền */}
      <section className="text-right">
        <p className="text-xl font-bold">Tổng cộng: {total.toLocaleString()} đ</p>
      </section>
    </div>
  );
};

export default CheckoutPage;
