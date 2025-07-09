// src/pages/RegisterPage.js
import React from 'react';
import { useForm } from 'react-hook-form';
import { register as registerApi } from '../services/authService';
import { useNavigate } from 'react-router-dom';

const RegisterPage = () => {
  const navigate = useNavigate();
  const { register, handleSubmit, formState: { errors } } = useForm();

  const onSubmit = async (data) => {
    try {
      await registerApi(data);
      alert('Đăng ký thành công!');
      navigate('/login');
    } catch (error) {
      alert(error.response?.data?.error || 'Đăng ký thất bại');
    }
  };

  return (
    <div className="max-w-md mx-auto mt-10 p-6 shadow rounded bg-white">
      <h2 className="text-xl font-bold mb-4">Đăng ký tài khoản</h2>
      <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
        <input {...register("user_name", { required: true })} placeholder="Họ tên" className="input" />
        {errors.user_name && <p className="text-red-500">Tên không được để trống</p>}

        <input {...register("user_email", { required: true })} placeholder="Email" className="input" />
        {errors.user_email && <p className="text-red-500">Email không hợp lệ</p>}

        <input {...register("user_phone", { required: true })} placeholder="Số điện thoại" className="input" />
        {errors.user_phone && <p className="text-red-500">SĐT không được để trống</p>}

        <input {...register("user_address", { required: true })} placeholder="Địa chỉ" className="input" />
        {errors.user_address && <p className="text-red-500">Địa chỉ không được để trống</p>}

        <input {...register("password_hash", { required: true, minLength: 6 })} type="password" placeholder="Mật khẩu" className="input" />
        {errors.password_hash && <p className="text-red-500">Mật khẩu tối thiểu 6 ký tự</p>}

        <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">Đăng ký</button>
      </form>
    </div>
  );
};

export default RegisterPage;
