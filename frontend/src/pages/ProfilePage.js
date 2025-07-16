// pages/ProfilePage.jsx
import React, { useEffect, useState } from 'react';
import { getProfile, updateProfile } from '../api/userApi';

const ProfilePage = () => {
  const [userData, setUserData] = useState(null);
  const [isEditing, setIsEditing] = useState(false);

  const fetchUser = async () => {
    try {
      const res = await getProfile();
      setUserData(res.data);
    } catch (err) {
      console.error("Lỗi lấy thông tin:", err);
    }
  };

  useEffect(() => {
    fetchUser();
  }, []);

  const handleChange = (e) => {
    setUserData({ ...userData, [e.target.name]: e.target.value });
  };

  const handleSave = async () => {
    try {
      await updateProfile(userData);
      setIsEditing(false);
    } catch (err) {
      alert('Cập nhật thất bại!');
    }
  };

  if (!userData) return <div>Đang tải...</div>;

  return (
    <div className="max-w-md mx-auto mt-10 bg-white shadow p-6 rounded">
      <h2 className="text-2xl font-bold mb-4">👤 Thông tin cá nhân</h2>
      <div className="space-y-4">
        <div>
          <label>Email:</label>
          <input
            disabled
            value={userData.user_email}
            className="w-full p-2 border rounded bg-gray-100"
          />
        </div>
        <div>
          <label>Họ tên:</label>
          <input
            name="user_name"
            value={userData.user_name}
            onChange={handleChange}
            disabled={!isEditing}
            className="w-full p-2 border rounded"
          />
        </div>
        <div>
          <label>Số điện thoại:</label>
          <input
            name="user_phone"
            value={userData.user_phone}
            onChange={handleChange}
            disabled={!isEditing}
            className="w-full p-2 border rounded"
          />
        </div>
        <div>
          <label>Địa chỉ:</label>
          <input
            name="user_address"
            value={userData.user_address}
            onChange={handleChange}
            disabled={!isEditing}
            className="w-full p-2 border rounded"
          />
        </div>

        <div className="flex justify-end gap-2">
          {isEditing ? (
            <>
              <button onClick={() => setIsEditing(false)} className="px-4 py-2 bg-gray-400 text-white rounded">Hủy</button>
              <button onClick={handleSave} className="px-4 py-2 bg-green-600 text-white rounded">Lưu</button>
            </>
          ) : (
            <button onClick={() => setIsEditing(true)} className="px-4 py-2 bg-blue-600 text-white rounded">Thay đổi</button>
          )}
        </div>
      </div>
    </div>
  );
};

export default ProfilePage;
