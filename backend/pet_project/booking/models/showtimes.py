from django.db import models
from booking.models.movies import Movies
from booking.models.rooms import Rooms

class Showtimes(models.Model):
    movie = models.ForeignKey(Movies, models.DO_NOTHING)
    room = models.ForeignKey(Rooms, models.DO_NOTHING)
    start_time = models.DateTimeField()
    base_price = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)  
    update_at = models.DateTimeField(auto_now=True)  

    class Meta:
        managed = True
        db_table = 'showtimes'
        verbose_name = 'Showtime'
    
    def __str__(self):
        return f"{self.movie.title} - {self.room.room_name} - {self.start_time.strftime('%Y-%m-%d %H:%M')}"
        