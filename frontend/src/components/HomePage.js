import React, { useEffect, useState } from 'react';

import axios from 'axios';

import { Card, CardContent } from '@/components/ui/card';

import { Badge } from '@/components/ui/badge';



const HomePage = () => {

  const [movies, setMovies] = useState([]);

  const [isLoading, setIsLoading] = useState(true);



  useEffect(() => {

    axios.get('http://localhost:8000/api/movies/now-showing/')

      .then((res) => {

        setMovies(res.data);

        setIsLoading(false);

      })

      .catch((err) => {

        console.error('Failed to fetch movies:', err);

        setIsLoading(false);

      });

  }, []);



  if (isLoading) return <p className="text-center text-xl mt-10">Đang tải phim...</p>;



  return (

    <div className="p-6">

      <h2 className="text-3xl font-bold mb-6 text-center">PHIM ĐANG CHIẾU</h2>

      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">

        {movies.map((movie) => (

          <Card key={movie.id} className="rounded-2xl shadow-md">

            <img src={movie.poster_url} alt={movie.title} className="w-full h-80 object-cover rounded-t-2xl" />

            <CardContent className="p-4">

              <div className="flex items-center justify-between mb-2">

                <span className="text-sm font-medium text-gray-500">T{movie.age_rating}</span>

                {movie.is_hot && <Badge variant="destructive">HOT</Badge>}

              </div>

              <h3 className="text-lg font-semibold mb-1 text-blue-700 hover:underline cursor-pointer">

                {movie.title}

              </h3>

              <p className="text-sm text-gray-600">Thể loại: {movie.genre}</p>

              <p className="text-sm text-gray-600">Thời lượng: {movie.duration} phút</p>

            </CardContent>

          </Card>

        ))}

      </div>

    </div>

  );

};



export default HomePage;
