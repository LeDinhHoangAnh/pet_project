import React from 'react';
import { useForm } from 'react-hook-form';
import { register as registerApi } from '../services/authService';
import { useNavigate } from 'react-router-dom';
import { FaUser, FaEnvelope, FaPhone, FaLock, FaHome } from 'react-icons/fa';

const RegisterPage = () => {
  const navigate = useNavigate();

  const {
    register,
    handleSubmit,
    setError,
    formState: { errors },
  } = useForm();

  const onSubmit = async (data) => {
    try {
      await registerApi(data);
      alert('Đăng ký thành công!');
      navigate('/login');
    } catch (error) {
      let errMsg = error.response?.data?.error || 'Đăng ký thất bại';

      if (typeof errMsg === 'string') {
      errMsg = errMsg.replace(/[\[\]']+/g, '').trim(); // Xoá [, ], '
      }
      if (errMsg.includes("Email")) {
        setError("user_email", { type: "manual", message: errMsg });
      } else if (errMsg.includes("Số điện thoại")) {
        setError("user_phone", { type: "manual", message: errMsg });
      } else {
        alert(errMsg);
      }
    }
  };

  const renderInput = (icon, placeholder, name, type = "text", validate = {}) => (
    <div className="flex items-center border rounded px-3 py-2 bg-white">
      {icon}
      <input
        {...register(name, validate)}
        type={type}
        placeholder={placeholder}
        className="flex-1 ml-2 outline-none"
      />
    </div>
  );

  return (
    <div className="max-w-md mx-auto mt-14 p-6 shadow rounded bg-gray-50">
      <h2 className="text-2xl font-bold mb-6 text-center">🎬 Đăng ký tài khoản</h2>
      <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
        {renderInput(<FaUser />, "Họ tên", "user_name", "text", {
          required: "Tên không được để trống",
        })}
        {errors.user_name && (
          <p className="text-red-500 text-sm">{errors.user_name.message}</p>
        )}

        {renderInput(<FaEnvelope />, "Email", "user_email", "email", {
          required: "Email không được để trống",
        })}
        {errors.user_email && (
          <p className="text-red-500 text-sm">{errors.user_email.message}</p>
        )}

        {renderInput(<FaPhone />, "Số điện thoại", "user_phone", "text", {
          required: "Số điện thoại không được để trống",
        })}
        {errors.user_phone && (
          <p className="text-red-500 text-sm">{errors.user_phone.message}</p>
        )}

        {renderInput(<FaHome />, "Địa chỉ", "user_address", "text", {
          required: "Địa chỉ không được để trống",
        })}
        {errors.user_address && (
          <p className="text-red-500 text-sm">{errors.user_address.message}</p>
        )}

        {renderInput(<FaLock />, "Mật khẩu", "password", "password", {
          required: "Mật khẩu không được để trống",
          minLength: {
            value: 8,
            message: "Mật khẩu tối thiểu 8 ký tự",
          },
        })}
        {errors.password && (
          <p className="text-red-500 text-sm">{errors.password.message}</p>
        )}

        <button
          type="submit"
          className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700"
        >
          Đăng ký
        </button>
      </form>
    </div>
  );
};

export default RegisterPage;
