// src/pages/ProfilePage.js
import React, { useEffect, useState } from 'react';
import { getProfile, updateProfile } from '../api/userApi';
import { getCurrentUser } from '../utils/auth';

const ProfilePage = () => {
  const [formData, setFormData] = useState({
    user_name: '',
    user_phone: '',
    user_address: '',
    user_email: '',
  });
  const [editMode, setEditMode] = useState(false);
  const [originalData, setOriginalData] = useState({});
  const [message, setMessage] = useState(null);

  const user = getCurrentUser(); // lấy user từ localStorage
  console.log(user)
  useEffect(() => {
    if (user && user.email) {
      getProfile(user.email) // truyền email hiện tại vào API
        .then((data) => {
          setFormData(data);
          setOriginalData(data);
        })
        .catch((err) => {
          console.error(err);
          setMessage('Không thể tải thông tin người dùng');
        });
    }
  }, [user]);

  const handleChange = (e) => {
    setFormData((prev) => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await updateProfile(formData);
      setEditMode(false);
      setMessage('✅ Cập nhật thành công!');
      setOriginalData(formData);
    } catch (err) {
      const msg = err.response?.data?.error || '❌ Lỗi khi cập nhật.';
      setMessage(msg);
    }
  };

  const handleCancel = () => {
    setFormData(originalData);
    setEditMode(false);
    setMessage(null);
  };

  return (
    <div className="max-w-xl mx-auto mt-10 p-6 bg-white rounded shadow">
      <h2 className="text-2xl font-bold mb-6">👤 Thông tin cá nhân</h2>
      {message && <p className="mb-4 text-blue-600">{message}</p>}

      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block font-medium">Tên người dùng</label>
          <input
            type="text"
            name="user_name"
            value={formData.user_name}
            onChange={handleChange}
            className="w-full border px-3 py-2 rounded"
            disabled={!editMode}
            required
          />
        </div>

        <div>
          <label className="block font-medium">Số điện thoại</label>
          <input
            type="text"
            name="user_phone"
            value={formData.user_phone}
            onChange={handleChange}
            className="w-full border px-3 py-2 rounded"
            disabled={!editMode}
            required
          />
        </div>

        <div>
          <label className="block font-medium">Địa chỉ</label>
          <input
            type="text"
            name="user_address"
            value={formData.user_address}
            onChange={handleChange}
            className="w-full border px-3 py-2 rounded"
            disabled={!editMode}
          />
        </div>

        <div>
          <label className="block font-medium text-gray-500">Email</label>
          <input
            type="text"
            name="user_email"
            value={formData.user_email}
            disabled
            className="w-full border px-3 py-2 rounded bg-gray-100 cursor-not-allowed"
          />
        </div>

        {!editMode ? (
          <button
            type="button"
            onClick={() => setEditMode(true)}
            className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
          >
            Thay đổi thông tin
          </button>
        ) : (
          <div className="flex gap-4">
            <button
              type="button"
              onClick={handleCancel}
              className="bg-gray-500 text-white px-4 py-2 rounded hover:bg-gray-600"
            >
              Hủy
            </button>
            <button
              type="submit"
              className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700"
            >
              Lưu
            </button>
          </div>
        )}
      </form>
    </div>
  );
};

export default ProfilePage;
