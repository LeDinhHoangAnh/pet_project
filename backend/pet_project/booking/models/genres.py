from django.db import models

class Genres(models.Model):
    genre_name = models.CharField(unique=True, max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)  
    update_at = models.DateTimeField(auto_now=True)  

    class Meta:
        managed = True
        db_table = 'genres'
        verbose_name = 'Genre'
    def __str__(self):
        return f"{self.genre_name}"
    
