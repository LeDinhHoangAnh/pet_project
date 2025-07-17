from django.db import models
from booking.models.bookings import Bookings

class BookingDetails(models.Model):
    booking = models.ForeignKey('Bookings', models.DO_NOTHING)
    seat = models.ForeignKey('Seats', models.DO_NOTHING)
    create_at = models.DateTimeField(auto_now_add=True)  
    update_at = models.DateTimeField(auto_now=True)  

    class Meta:
        managed = True
        db_table = 'booking_details'
        unique_together = (('booking', 'seat'),)
        verbose_name = 'Booking Detail'