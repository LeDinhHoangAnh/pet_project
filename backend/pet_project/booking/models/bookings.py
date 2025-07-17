from django.db import models
from booking.models.users import Users
from booking.models.admins import Admins
from booking.models.showtimes import Showtimes

class Bookings(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    showtime = models.ForeignKey('Showtimes', models.DO_NOTHING)
    total_price = models.IntegerField()
    booking_status = models.CharField(max_length=50)
    booking_type = models.CharField(max_length=7)
    admin = models.ForeignKey(Admins, models.DO_NOTHING, blank=True, null=True)
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    customer_phone = models.CharField(max_length=10, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)  
    update_at = models.DateTimeField(auto_now=True)  

    class Meta:
        managed = True
        db_table = 'bookings'
        verbose_name = 'Booking'
    def __str__(self):
        return f"{self.showtime} - {self.user}"