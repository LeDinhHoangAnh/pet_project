from django.db import models
from booking.models.showtimes import Showtimes
from booking.models.seat_types import SeatTypes

class SeatPrices(models.Model):
    showtime = models.ForeignKey('Showtimes', models.DO_NOTHING)
    seat_type = models.ForeignKey('SeatTypes', models.DO_NOTHING)
    price = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)  
    update_at = models.DateTimeField(auto_now=True)  

    class Meta:
        managed = True
        db_table = 'seat_prices'
        verbose_name = 'Seat Price'
    def __str__(self):
        return f"{self.seat_type} - {self.price}"
    
