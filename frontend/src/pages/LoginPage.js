// src/pages/LoginPage.js
import React from 'react';
import { useForm } from 'react-hook-form';
import { login } from '../services/authService';
import { saveToken, decodeToken } from '../utils/auth';
import { useNavigate } from 'react-router-dom';

const LoginPage = () => {
  const navigate = useNavigate();
  const { register, handleSubmit, formState: { errors } } = useForm();

  const onSubmit = async (data) => {
    try {
      const res = await login(data);
      const token = res.data.token;
      saveToken(token);

      const user = decodeToken();
      if (user.role === 'admin') {
        navigate('/admin');
      } else {
        navigate('/');
      }
    } catch (error) {
      alert('Đăng nhập thất bại. Kiểm tra lại thông tin!');
    }
  };

  return (
    <div className="max-w-md mx-auto mt-10 p-6 shadow rounded bg-white">
      <h2 className="text-xl font-bold mb-4">Đăng nhập</h2>
      <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
        <input {...register("email", { required: true })} placeholder="Email" className="input" />
        {errors.email && <p className="text-red-500">Email không được để trống</p>}

        <input {...register("password", { required: true })} type="password" placeholder="Mật khẩu" className="input" />
        {errors.password && <p className="text-red-500">Mật khẩu không được để trống</p>}

        <button type="submit" className="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600">Đăng nhập</button>
      </form>
    </div>
  );
};

export default LoginPage;
