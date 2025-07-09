from django.contrib.auth.hashers import check_password
from booking.repos.user_repo import get_user_by_email

def authenticate_user(email, password):
    user = get_user_by_email(email)
    if user and check_password(password, user.password_hash):
        return user
    return None