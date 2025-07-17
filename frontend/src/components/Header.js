// src/components/Header.js
import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { isLoggedIn, getCurrentUser, logout } from '../utils/auth';

const Header = () => {
  const navigate = useNavigate();
  const user = getCurrentUser();
  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <header className="bg-black text-white p-4 shadow-md fixed top-0 left-0 w-full z-50">
      <div className="container mx-auto flex justify-between items-center">
        <h1 className="text-xl font-bold"><Link to="/">🎬 MovieBooking</Link></h1>
        <nav>
          <ul className="flex space-x-4">
            <li><Link to="/">Trang chủ</Link></li>
            <li><Link to="/movie-schedule">Lịch chiếu</Link></li>
            <li><Link to="/phim">Phim</Link></li>
            <li><Link to="/history">Thông tin đặt vé</Link></li>
            {!isLoggedIn() ? (
              <>
                <li><Link to="/login">Đăng nhập</Link></li>
                <li><Link to="/register">Đăng ký</Link></li>
              </>
            ) : (
              <>
                <li>
                  <Link to="/profile" className="hover:underline">
                    👋 Xin chào, <strong>{user?.user_name || 'User'}</strong>
                  </Link>
                </li>
                <li>
                  <button onClick={handleLogout} className="text-red-400 hover:underline">
                    Đăng xuất
                  </button>
                </li>
              </>
            )}
          </ul>
        </nav>
      </div>
    </header>
  );
};

export default Header;
