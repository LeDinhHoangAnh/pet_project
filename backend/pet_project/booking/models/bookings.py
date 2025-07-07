from django.db import models
from booking.models.users import Users
from booking.models.admins import Admins
from booking.models.showtimes import Showtimes

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
        managed = True
        db_table = 'bookings'