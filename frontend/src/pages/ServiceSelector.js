// src/pages/ServiceSelector.js
import React, { useEffect } from 'react';
import axios from 'axios';

const ServiceSelector = ({ totalSeatPrice, services, setServices, quantities, setQuantities }) => {
  const BASE_URL = process.env.REACT_APP_API_BASE_URL;

  useEffect(() => {
    const fetchServices = async () => {
      try {
        const res = await axios.get(`${BASE_URL}/api/services/`);
        setServices(res.data);
      } catch (err) {
        console.error('Lỗi khi tải dịch vụ:', err);
      }
    };
    if (services.length === 0) {
      fetchServices();
    }
  }, []);

  const handleQuantityChange = (id, delta) => {
    setQuantities((prev) => {
      const next = { ...prev };
      next[id] = Math.max(0, (next[id] || 0) + delta);
      return next;
    });
  };

  const totalServicePrice = services.reduce((sum, s) => {
    const qty = quantities[s.id] || 0;
    return sum + qty * s.service_price;
  }, 0);

  return (
    <div className="md:col-span-2 bg-gray-100 p-4 rounded shadow">
      <h2 className="text-xl font-bold mb-4">Chọn dịch vụ</h2>
      <div className="flex flex-col gap-4">
        {/* Dòng tiêu đề */}
        <div className="flex items-center border-b pb-2 font-semibold text-gray-700 gap-6">
          <div className="w-20" /> {/* Cột hình ảnh, để trống */}
          <div className="w-1/4">Tên dịch vụ</div>
          <div className="w-1/3">Mô tả</div>
          <div className="w-1/6">Giá</div>
          <div className="w-32">Số lượng</div>
        </div>

        {/* Dòng dữ liệu */}
        {services.map(service => (
          <div key={service.id} className="flex items-center border p-3 rounded gap-6">
            <img
              src={`${BASE_URL}${service.service_image_url}`}
              alt={service.service_name}
              className="w-20 h-20 object-cover rounded"
            />
            <div className="w-1/4">
              <h4 className="font-medium">{service.service_name}</h4>
            </div>
            <div className="w-1/3 text-sm text-gray-600">{service.service_description}</div>
            <div className="w-1/6 font-medium text-green-600">
              {service.service_price.toLocaleString()} đ
            </div>
            <div className="flex items-center gap-2 w-32">
              <button
                className="bg-gray-300 px-2 rounded"
                onClick={() => handleQuantityChange(service.id, -1)}
              >-</button>
              <span>{quantities[service.id] || 0}</span>
              <button
                className="bg-gray-300 px-2 rounded"
                onClick={() => handleQuantityChange(service.id, 1)}
              >+</button>
            </div>
          </div>
        ))}
      </div>

      <div className="mt-6 text-right">
        <p className="mb-2">Tổng tiền ghế: <strong>{totalSeatPrice.toLocaleString()} đ</strong></p>
        <p className="mb-2">Tổng dịch vụ: <strong>{totalServicePrice.toLocaleString()} đ</strong></p>
      </div>
    </div>
  );
};

export default ServiceSelector;
