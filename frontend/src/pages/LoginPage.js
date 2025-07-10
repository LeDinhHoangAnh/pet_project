import React from 'react';
import { useForm } from 'react-hook-form';
import { login } from '../services/authService';
import { saveToken, decodeToken } from '../utils/auth';
import { useNavigate } from 'react-router-dom';
import { FaEnvelope, FaLock } from 'react-icons/fa';

const LoginPage = () => {
  const navigate = useNavigate();
  const { register, handleSubmit, formState: { errors } } = useForm();
  // const redirect = localStorage.getItem('redirect_after_login');
  //     if (redirect) {
  //       localStorage.removeItem('redirect_after_login');
  //       navigate(redirect);
  //     } else {
  //       navigate('/');
  //     }

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
  <div className="max-w-md mx-auto mt-14 p-6 shadow rounded bg-gray-50">
      <h2 className="text-2xl font-bold mb-6 text-center">🔐 Đăng nhập</h2>
      <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
        <div className="flex items-center border rounded px-3 py-2 bg-white">
          <FaEnvelope />
          <input
            {...register("user_email", { required: true })}
            placeholder="Email"
            className="flex-1 ml-2 outline-none"
          />
        </div>
        {errors.user_email && <p className="text-red-500 text-sm">Email không được để trống</p>}

        <div className="flex items-center border rounded px-3 py-2 bg-white">
          <FaLock />
          <input
            {...register("password", { required: true })}
            type="password"
            placeholder="Mật khẩu"
            className="flex-1 ml-2 outline-none"
          />
        </div>
        {errors.password && <p className="text-red-500 text-sm">Mật khẩu không được để trống</p>}

        <button type="submit" className="w-full bg-green-600 text-white py-2 rounded hover:bg-green-700">
          Đăng nhập
        </button>
      </form>
    </div>
  );
};

export default LoginPage;
