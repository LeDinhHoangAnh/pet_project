// src/components/BookingActions.js
import React from 'react';

const BookingActions = ({ step, onBack, onNext, onCheckout, canProceed }) => {
  return (
    <div className="mt-6 w-full">
      {step === 'select-seat' && (
        <button
          onClick={onNext}
          className="w-full bg-green-600 text-white py-2 rounded hover:bg-green-700 transition"
          disabled={!canProceed}
        >
          Tiếp tục
        </button>
      )}
      {step === 'select-service' && (
        <div className="flex gap-2">
          <button onClick={onBack} className="flex-1 bg-gray-500 text-white py-2 rounded hover:bg-gray-600 transition">Quay lại</button>
          <button onClick={onNext} className="flex-1 bg-green-600 text-white py-2 rounded hover:bg-green-700 transition">Tiếp tục</button>
        </div>
      )}
      {step === 'checkout' && (
        <div className="flex gap-2">
          <button onClick={onBack} className="flex-1 bg-gray-500 text-white py-2 rounded hover:bg-gray-600 transition">Quay lại</button>
          <button onClick={onCheckout} className="flex-1 bg-blue-600 text-white py-2 rounded hover:bg-blue-700 transition">Thanh toán</button>
        </div>
      )}
    </div>
  );
};

export default BookingActions;
