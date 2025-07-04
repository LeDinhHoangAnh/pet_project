from django.db import models
from booking.models.movies import Movies
from booking.models.rooms import Rooms

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
        