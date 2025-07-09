import React from 'react';

const TrailerModal = ({ trailerUrl, movieTitle, onClose }) => {
  if (!trailerUrl) return null;

  const youtubeId = trailerUrl.split('v=')[1]?.split('&')[0];

  return (
    <div className="fixed inset-0 bg-black bg-opacity-70 flex items-center justify-center z-50">
      <div className="bg-white p-4 rounded-lg relative w-[90vw] max-w-5xl shadow-lg">
        <button
          onClick={onClose}
          className="absolute top-2 right-2 text-black text-xl font-bold hover:text-red-600"
        >
          ✖
        </button>

        {/* Tiêu đề phim */}
        <h2 className="text-xl font-bold text-center mb-4 text-gray-800">
          🎬 Trailer: {movieTitle}
        </h2>

        <div className="w-full aspect-video">
          {youtubeId ? (
            <iframe
              width="100%"
              height="100%"
              src={`https://www.youtube.com/embed/${youtubeId}`}
              title="Trailer"
              frameBorder="0"
              allowFullScreen
              className="rounded-md"
            />
          ) : (
            <p className="text-center text-red-600">Không thể hiển thị trailer</p>
          )}
        </div>
      </div>
    </div>
  );
};

export default TrailerModal;
