import React from 'react';
import '../styles/Header.css';
import { Link, useNavigate } from 'react-router-dom';

const Header = () => {
  const navigate = useNavigate();

  // Lấy thông tin người dùng từ localStorage
  const user = JSON.parse(localStorage.getItem('user'));

  const handleLogout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    navigate('/login');
    window.location.reload(); // làm mới để cập nhật header
  };

  return (
    <header className="bg-black text-white p-4 shadow-md fixed top-0 left-0 w-full z-50">
      <div className="container mx-auto flex justify-between items-center">
        <h1 className="logo text-xl font-bold">🎬 MovieBooking</h1>

        <nav>
          <ul className="menu flex space-x-4 items-center">
            <li><Link to="/">Trang chủ</Link></li>
            <li><Link to="/lich-chieu">Lịch chiếu</Link></li>
            <li><Link to="/phim">Phim</Link></li>
            <li><Link to="/rap">Rạp</Link></li>
            <li><Link to="/dat-ve">Đặt vé</Link></li>
            <li><Link to="/gioi-thieu">Giới thiệu</Link></li>

            {!user ? (
              <>
                <li><Link to="/login" className="hover:underline">Đăng nhập</Link></li>
                <li><Link to="/register" className="hover:underline">Đăng ký</Link></li>
              </>
            ) : (
              <li className="relative group">
                <span className="font-medium cursor-pointer">
                  👤 {user.user_name}
                </span>
                <div className="absolute hidden group-hover:block bg-white text-black right-0 mt-2 rounded shadow-md min-w-[150px] z-50">
                  <button
                    onClick={handleLogout}
                    className="block w-full text-left px-4 py-2 hover:bg-gray-100"
                  >
                    Đăng xuất
                  </button>
                </div>
              </li>
            )}
          </ul>
        </nav>
      </div>
    </header>
  );
};

export default Header;
