from django.contrib.auth.hashers import check_password
from booking.repos.user_repo import get_user_by_email
from booking.models.users import Users, Roles
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError

def authenticate_user(email, password):
    user = get_user_by_email(email)
    if user and check_password(password, user.password_hash):
        return user
    return None


def create_user(data):
    email = data.get('user_email')
    phone = data.get('user_phone')

    if Users.objects.filter(user_email=email).exists():
        raise ValidationError("Email đã được sử dụng")

    if Users.objects.filter(user_phone=phone).exists():
        raise ValidationError("Số điện thoại đã được sử dụng")

    user = Users.objects.create(
        user_name=data.get('user_name'),
        user_email=email,
        user_phone=phone,
        user_address=data.get('user_address'),
        password_hash=make_password(data.get('password')),  # ✅ hash mật khẩu
        role_id=2,  # Giả sử role ID 2 là 'User'
    )
    return user