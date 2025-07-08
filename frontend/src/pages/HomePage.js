// src/pages/HomePage.js
import React from 'react';
import Header from '../components/Header';
import BannerSlider from '../components/BannerSlider';
import MovieList from '../components/MovieList';

const HomePage = () => (
  <>
    <Header />
    <BannerSlider />
    <MovieList />
  </>
);

export default HomePage;
