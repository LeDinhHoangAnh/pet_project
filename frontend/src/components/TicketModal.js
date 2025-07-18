import React from 'react';
const formatDateDMY = (isoDate) => {
  const d = new Date(isoDate);
  const day = String(d.getDate()).padStart(2, '0');
  const month = String(d.getMonth() + 1).padStart(2, '0');
  const year = d.getFullYear();
  return `${day}-${month}-${year}`;
};

const TicketModal = ({ show, onClose, showtime }) => {
  if (!show) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-white rounded-2xl shadow-xl w-full max-w-md p-6 relative animate-fade-in">
        <div className="mb-4 border-b pb-3">
          <h2 className="text-2xl font-bold text-blue-700 flex items-center gap-2">
            🎟️ Mua Vé
          </h2>
        </div>

        <div className="space-y-2 text-gray-700 text-sm">
          <div className="flex justify-between">
            <span className="font-semibold">🎬 Phim:</span>
            <span>{showtime?.movie?.title || 'Không có tên phim'}</span>
          </div>
          <div className="flex justify-between">
            <span className="font-semibold">📅 Ngày chiếu:</span>
            <span>{formatDateDMY(showtime.start_time)}</span>
          </div>
          <div className="flex justify-between">
            <span className="font-semibold">⏰ Giờ chiếu:</span>
            <span>
              {new Date(showtime.start_time).toLocaleTimeString([], {
                hour: '2-digit',
                minute: '2-digit',
                hour12: false,
              })}
            </span>
          </div>
        </div>

        <div className="flex justify-end gap-3 mt-6">
          <button
            className="px-4 py-2 rounded-xl bg-gray-200 text-gray-800 hover:bg-gray-300 transition"
            onClick={onClose}
          >
            Đóng
          </button>
          <button
            className="px-4 py-2 rounded-xl bg-blue-600 text-white hover:bg-blue-700 transition"
            onClick={() => {
              const token = localStorage.getItem('token');
              if (token) {
                window.location.href = `/booking/${showtime.id}`;
              } else {
                localStorage.setItem('redirect_after_login', `/booking/${showtime.id}`);
                window.location.href = '/login';
              }
            }}
          >
            Mua vé
          </button>
        </div>
      </div>
    </div>
  );
};

export default TicketModal;
