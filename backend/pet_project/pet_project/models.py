# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admins(models.Model):
    admin_name = models.CharField(max_length=100)
    admin_email = models.CharField(unique=True, max_length=100)
    admin_password_hash = models.CharField(max_length=255)
    role = models.ForeignKey('Roles', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admins'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BookingDetails(models.Model):
    booking = models.ForeignKey('Bookings', models.DO_NOTHING)
    seat = models.ForeignKey('Seats', models.DO_NOTHING)
    create_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking_details'
        unique_together = (('booking', 'seat'),)


class BookingServices(models.Model):
    booking = models.ForeignKey('Bookings', models.DO_NOTHING)
    service = models.ForeignKey('Services', models.DO_NOTHING)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
    create_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking_services'


class Bookings(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    showtime = models.ForeignKey('Showtimes', models.DO_NOTHING)
    total_price = models.IntegerField()
    booking_status = models.CharField(max_length=50)
    create_at = models.DateTimeField(blank=True, null=True)
    booking_type = models.CharField(max_length=7)
    admin = models.ForeignKey(Admins, models.DO_NOTHING, blank=True, null=True)
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    customer_phone = models.CharField(max_length=10, blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bookings'


class Cinemas(models.Model):
    cinemas_name = models.CharField(max_length=100)
    cinemas_address = models.CharField(max_length=255)
    create_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cinemas'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Genres(models.Model):
    genre_name = models.CharField(unique=True, max_length=255)
    create_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genres'


class Movies(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    duration = models.IntegerField()
    age_rating = models.CharField(max_length=10, blank=True, null=True)
    trailer_url = models.TextField(blank=True, null=True)
    movie_poster_url = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movies'


class MoviesGenres(models.Model):
    movie = models.OneToOneField(Movies, models.DO_NOTHING, primary_key=True)  # The composite primary key (movie_id, genre_id) found, that is not supported. The first column is selected.
    genre = models.ForeignKey(Genres, models.DO_NOTHING)
    create_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movies_genres'
        unique_together = (('movie', 'genre'),)


class Payments(models.Model):
    booking = models.ForeignKey(Bookings, models.DO_NOTHING)
    method = models.CharField(max_length=50)
    amount = models.IntegerField()
    status = models.CharField(max_length=20, blank=True, null=True)
    payment_transaction_code = models.CharField(max_length=100, blank=True, null=True)
    paid_at = models.DateTimeField(blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payments'


class Permissions(models.Model):
    permission_name = models.CharField(unique=True, max_length=100)
    permission_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissions'


class RolePermissions(models.Model):
    role = models.OneToOneField('Roles', models.DO_NOTHING, primary_key=True)  # The composite primary key (role_id, permission_id) found, that is not supported. The first column is selected.
    permission = models.ForeignKey(Permissions, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'role_permissions'
        unique_together = (('role', 'permission'),)


class Roles(models.Model):
    role_name = models.CharField(unique=True, max_length=50)
    create_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Rooms(models.Model):
    room_name = models.CharField(max_length=100)
    room_number = models.CharField(max_length=10)
    cinema = models.ForeignKey(Cinemas, models.DO_NOTHING)
    create_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rooms'


class SeatPrices(models.Model):
    showtime = models.ForeignKey('Showtimes', models.DO_NOTHING)
    seat_type = models.ForeignKey('SeatTypes', models.DO_NOTHING)
    price = models.IntegerField()
    create_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seat_prices'


class SeatTypes(models.Model):
    seat_type_name = models.CharField(unique=True, max_length=50)
    seat_type_description = models.TextField(blank=True, null=True)
    seat_type_color_code = models.CharField(max_length=10, blank=True, null=True)
    seat_type_status = models.CharField(max_length=20, blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seat_types'


class Seats(models.Model):
    room = models.ForeignKey(Rooms, models.DO_NOTHING)
    seat_type = models.ForeignKey(SeatTypes, models.DO_NOTHING)
    seat_number = models.CharField(max_length=10)
    create_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seats'


class Services(models.Model):
    service_name = models.CharField(max_length=100)
    service_description = models.TextField(blank=True, null=True)
    service_price = models.IntegerField()
    service_image_url = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services'


class Showtimes(models.Model):
    movie = models.ForeignKey(Movies, models.DO_NOTHING)
    room = models.ForeignKey(Rooms, models.DO_NOTHING)
    start_time = models.DateTimeField()
    base_price = models.IntegerField()
    create_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'showtimes'
        


class Users(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    user_phone = models.CharField(max_length=10)
    user_address = models.CharField(max_length=255)
    password_hash = models.CharField(max_length=255)
    role = models.ForeignKey(Roles, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    account_type = models.CharField(max_length=50, blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
