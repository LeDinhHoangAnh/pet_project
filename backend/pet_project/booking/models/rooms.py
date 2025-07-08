from django.db import models
from booking.models.cinemas import Cinemas

class Rooms(models.Model):
    room_name = models.CharField(max_length=100)
    room_number = models.CharField(max_length=10)
    cinema = models.ForeignKey(Cinemas, models.DO_NOTHING)
    create_at = models.DateTimeField(auto_now_add=True)  
    update_at = models.DateTimeField(auto_now=True)  

    class Meta:
        managed = True
        db_table = 'rooms'
        verbose_name = 'Room'
    
    def __str__(self):
        return f"{self.room_name} - {self.room_number}"