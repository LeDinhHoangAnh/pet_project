import React from 'react';
import { FaYoutube, FaFacebookF, FaTiktok, FaMapMarkerAlt, FaPhoneAlt } from 'react-icons/fa';

const Footer = () => {
  return (
    <footer className="bg-gray-900 text-white py-8">
      <div className="container mx-auto px-4 grid grid-cols-1 md:grid-cols-3 gap-6">
        
        {/* Thông tin liên hệ */}
        <div>
          <h2 className="text-xl font-bold mb-3">🎬 MovieBooking</h2>
          <p>Hệ thống đặt vé xem phim trực tuyến</p>
          <p className="flex items-center mt-2">
            <FaMapMarkerAlt className="mr-2" /> 123 Nguyễn Trãi, Hà Nội
          </p>
          <p className="flex items-center mt-1">
            <FaPhoneAlt className="mr-2" /> 0987 654 321
          </p>
        </div>

        {/* Liên kết mạng xã hội */}
        <div>
          <h2 className="text-xl font-bold mb-3">📱 Mạng xã hội</h2>
          <ul className="space-y-2">
            <li>
              <a
                href="https://youtube.com"
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center hover:underline"
              >
                <FaYoutube className="mr-2 text-red-600" /> YouTube
              </a>
            </li>
            <li>
              <a
                href="https://facebook.com"
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center hover:underline"
              >
                <FaFacebookF className="mr-2 text-blue-500" /> Facebook
              </a>
            </li>
            <li>
              <a
                href="https://tiktok.com"
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center hover:underline"
              >
                <FaTiktok className="mr-2" /> TikTok
              </a>
            </li>
          </ul>
        </div>

        {/* Thông tin thêm */}
        <div>
          <h2 className="text-xl font-bold mb-3">📌 Thông tin thêm</h2>
          <ul className="space-y-2 text-sm">
            <li>Chính sách bảo mật</li>
            <li>Điều khoản sử dụng</li>
            <li>Hợp tác phát hành phim</li>
            <li>Liên hệ quảng cáo</li>
          </ul>
        </div>
      </div>

      <div className="text-center text-gray-400 text-sm mt-6">
        © 2025 MovieBooking. All rights reserved.
      </div>
    </footer>
  );
};

export default Footer;
