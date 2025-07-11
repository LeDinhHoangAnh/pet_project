from django.db import models
from booking.models.showtimes import Showtimes
from booking.models.seats import Seats

class SeatStatusInShowtime(models.Model):
    showtime = models.ForeignKey('Showtimes', on_delete=models.CASCADE)
    seat = models.ForeignKey('Seats', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[
        ('booked', 'Booked')
    ])

    class Meta:
        unique_together = ('showtime', 'seat')
        db_table = 'seat_status_in_showtime'
        verbose_name = 'Seat in showtime'
