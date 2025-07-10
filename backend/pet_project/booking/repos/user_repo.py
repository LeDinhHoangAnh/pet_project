from booking.models.users import Users

def create_user(**kwargs):
    return Users.objects.create(**kwargs)

def get_user_by_email(email):
    try:
        return Users.objects.get(user_email=email)
    except Users.DoesNotExist:
        return None