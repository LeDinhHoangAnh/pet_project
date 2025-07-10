// src/components/Toast.js
import React, { useEffect } from 'react';

const Toast = ({ type = 'success', message, onClose }) => {
  useEffect(() => {
    const timer = setTimeout(() => {
      onClose(); // Gọi hàm xoá sau 3s
    }, 3000);
    return () => clearTimeout(timer); // Clear timeout nếu component bị huỷ
  }, [onClose]);

  return (
    <div className={`fixed top-5 right-5 z-50 px-4 py-3 rounded shadow-lg text-white 
      ${type === 'success' ? 'bg-green-500' : 'bg-red-500'}`}>
      {message}
    </div>
  );
};

export default Toast;
