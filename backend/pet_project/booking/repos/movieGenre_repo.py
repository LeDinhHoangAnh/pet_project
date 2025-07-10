from booking.models.movies_genres import MoviesGenres

def get_genres_by_movie(movie_id):
    return MoviesGenres.objects.filter(movie_id=movie_id).select_related('genre')
