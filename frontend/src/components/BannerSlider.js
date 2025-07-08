import React, { useEffect, useState } from 'react';
import Slider from "react-slick";
import { getAllMovies } from '../api/movieApi';
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

const BannerSlider = () => {
  const [banners, setBanners] = useState([]);
  const BASE_URL = 'http://localhost:8000'; // domain của Django server

  useEffect(() => {
    const fetchData = async () => {
      const data = await getAllMovies();
      setBanners(data);
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

  if (!banners.length) return <p>Đang tải banner...</p>;

  return (
    <div className="my-6">
      <Slider {...settings}>
        {banners.map((movie) => (
          <div key={movie.id}>
          <img
            src={`http://localhost:8000${movie.movie_poster_url}`}
            alt={movie.title}
            className="rounded-md w-full h-64 object-cover"
          />

            <div className="p-4 bg-black bg-opacity-60 text-white absolute bottom-0 w-full">
              <h2 className="text-xl font-bold">{movie.title}</h2>
              <p>{movie.description || 'Không có mô tả'}</p>
            </div>
          </div>
        ))}
      </Slider>
    </div>
  );
};

export default BannerSlider;
