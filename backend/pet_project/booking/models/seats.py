from django.db import models
from booking.models.rooms import Rooms
from booking.models.seat_types import SeatTypes

class Seats(models.Model):
    room = models.ForeignKey(Rooms, models.DO_NOTHING)
    seat_type = models.ForeignKey(SeatTypes, models.DO_NOTHING)
    seat_number = models.CharField(max_length=10)
    create_at = models.DateTimeField(auto_now_add=True)  
    update_at = models.DateTimeField(auto_now=True)  

    class Meta:
        managed = True
        db_table = 'seats'
        verbose_name = 'Seat'
    def __str__(self):
        return f"{self.seat_type} - {self.seat_number}"