from django.db import models
from booking.models.cinemas import Cinemas

class Rooms(models.Model):
    room_name = models.CharField(max_length=100)
    room_number = models.CharField(max_length=10)
    cinema = models.ForeignKey(Cinemas, models.DO_NOTHING)
    create_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rooms'