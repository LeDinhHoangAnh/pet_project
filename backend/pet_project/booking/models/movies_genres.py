from django.db import models
from booking.models.movies import Movies
from booking.models.genres import Genres

class MoviesGenres(models.Model):
    movie = models.OneToOneField(Movies, models.DO_NOTHING, primary_key=True)  # The composite primary key (movie_id, genre_id) found, that is not supported. The first column is selected.
    genre = models.ForeignKey(Genres, models.DO_NOTHING)
    create_at = models.DateTimeField(auto_now_add=True)  
    update_at = models.DateTimeField(auto_now=True)  

    class Meta:
        managed = True
        db_table = 'movies_genres'
        unique_together = (('movie', 'genre'),)
        verbose_name = 'Movie Genre'
    
    def __str__(self):
        return f"{self.movie} - {self.genre}"

