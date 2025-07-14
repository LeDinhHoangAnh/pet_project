from booking.models.users import Users

class UserProfileRepo:
    @staticmethod
    def get_by_id(user_id):
        return Users.objects.filter(id=user_id).first()

    @staticmethod
    def is_email_taken(email, exclude_user_id=None):
        qs = Users.objects.filter(user_email=email)
        if exclude_user_id:
            qs = qs.exclude(id=exclude_user_id)
        return qs.exists()

    @staticmethod
    def is_phone_taken(phone, exclude_user_id=None):
        qs = Users.objects.filter(user_phone=phone)
        if exclude_user_id:
            qs = qs.exclude(id=exclude_user_id)
        return qs.exists()

    @staticmethod
    def update_user(user, data):
        for key, value in data.items():
            setattr(user, key, value)
        user.save()
        return user

    @staticmethod
    def get_user_by_email(email):
        return Users.objects.filter(user_email=email).first()