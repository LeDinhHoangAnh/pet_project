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
    <div className="fixed inset-0 bg-black bg-opacity-40 flex items-center justify-center z-50">
      <div className="bg-white p-6 rounded-lg shadow-lg w-full max-w-md">
        <h2 className="text-xl font-semibold mb-4">🎟️ Mua Vé</h2>
        <p><strong>Phim:</strong> {showtime?.movie?.title || 'Không có tên phim'}</p>
        <p><strong>Ngày:</strong> {formatDateDMY(showtime.start_time)}</p>
        <strong>Giờ:</strong>{' '}
          {new Date(showtime.start_time).toLocaleTimeString([], {
            hour: '2-digit',
            minute: '2-digit',
            hour12: false, // 24h format
          })}

        <div className="flex justify-end gap-2 mt-6">
          <button
            className="bg-gray-300 px-4 py-2 rounded"
            onClick={onClose}
          >
            Đóng
          </button>
          <button
            className="bg-blue-600 text-white px-4 py-2 rounded"
            onClick={() => {
              const token = localStorage.getItem('token');
              if (token) {
                // Đã đăng nhập → chuyển đến trang mua vé
                window.location.href = `/booking/${showtime.id}`;
              } else {
                // Chưa đăng nhập → lưu lại showtimeId rồi chuyển đến login
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
