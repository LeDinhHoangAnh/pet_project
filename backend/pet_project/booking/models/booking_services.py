from django.db import models
from booking.models.bookings import Bookings
from booking.models.services import Services

class BookingServices(models.Model):
    booking = models.ForeignKey('Bookings', models.DO_NOTHING)
    service = models.ForeignKey('Services', models.DO_NOTHING)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)  
    update_at = models.DateTimeField(auto_now=True)  
    
    class Meta:
        managed = True
        db_table = 'booking_services'
        verbose_name = 'Booking Service'