from django.db import models
from booking.models.showtimes import Showtimes
from booking.models.seat_types import SeatTypes

class SeatPrices(models.Model):
    showtime = models.ForeignKey('Showtimes', models.DO_NOTHING)
    seat_type = models.ForeignKey('SeatTypes', models.DO_NOTHING)
    price = models.IntegerField()
    create_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seat_prices'
