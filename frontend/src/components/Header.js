import React from 'react';
import '../styles/Header.css';

const Header = () => (
  <header className="header">
    <div className="container">
      <h1 className="logo">🎬 MovieBooking</h1>
      <nav>
        <ul className="menu">
          <li><a href="/">Trang chủ</a></li>
          <li><a href="/lich-chieu">Lịch chiếu</a></li>
          <li><a href="/phim">Phim</a></li>
          <li><a href="/rap">Rạp</a></li>
          <li><a href="/dat-ve">Đặt vé</a></li>
          <li><a href="/gioi-thieu">Giới thiệu</a></li>
        </ul>
      </nav>
    </div>
  </header>
);

export default Header;
