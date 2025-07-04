from django.db import models
from booking.models.movies import Movies
from booking.models.genres import Genres

class MoviesGenres(models.Model):
    movie = models.OneToOneField(Movies, models.DO_NOTHING, primary_key=True)  # The composite primary key (movie_id, genre_id) found, that is not supported. The first column is selected.
    genre = models.ForeignKey(Genres, models.DO_NOTHING)
    create_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movies_genres'
        unique_together = (('movie', 'genre'),)
