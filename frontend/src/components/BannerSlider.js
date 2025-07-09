import React, { useEffect, useState } from 'react';
import Slider from "react-slick";
import { getAllMovies } from '../api/movieApi';
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

const BannerSlider = () => {
  const [banners, setBanners] = useState([]);
  const BASE_URL = process.env.REACT_APP_API_BASE_URL;

  useEffect(() => {
    const fetchData = async () => {
      const data = await getAllMovies();

      // Lọc 4 phim mới nhất dựa theo trường created_at
      const sorted = data
        .filter(movie => movie.update_at) // tránh undefined
        .sort((a, b) => new Date(b.update_at) - new Date(a.update_at))
        .slice(0, 4);

      setBanners(sorted);
    };
    fetchData();
  }, []);

  const settings = {
    dots: true,
    infinite: true,
    autoplay: true,
    arrows: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1
  };

  if (!banners.length) return <p className="text-center py-10">Đang tải banner...</p>;

  return (
    <div className="w-full h-[70vh] relative overflow-hidden">
      <Slider {...settings}>
        {banners.map((movie) => (
          <div key={movie.id} className="relative w-full h-[70vh]">
            <img
              src={`${BASE_URL}${movie.movie_poster_url}`}
              alt={movie.title}
              className="w-full h-full object-cover"
            />
            <div className="absolute bottom-0 w-full bg-black bg-opacity-60 text-white p-6">
              <h2 className="text-2xl font-bold">{movie.title}</h2>
              <p className="text-sm">{movie.description || 'Không có mô tả'}</p>
            </div>
          </div>
        ))}
      </Slider>
    </div>
  );
};

export default BannerSlider;
