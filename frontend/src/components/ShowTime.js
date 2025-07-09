import React from 'react';

const ShowtimeList = ({ showtimes }) => {
  if (!showtimes.length) return <p>Chưa có suất chiếu.</p>;

  return (
    <div className="mt-8">
      <h3 className="text-xl font-semibold mb-4">🎫 Suất chiếu</h3>
      <ul className="grid md:grid-cols-2 gap-4">
        {showtimes.map((show) => (
          <li key={show.id} className="border p-4 rounded shadow-sm">
            <p><strong>Thời gian:</strong> {new Date(show.start_time).toLocaleString()}</p>
            <p><strong>Giá vé:</strong> {show.base_price.toLocaleString()}đ</p>
            <p><strong>Phòng:</strong> {show.room.room_name}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ShowtimeList;
