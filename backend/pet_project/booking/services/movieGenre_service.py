from booking.repos.movieGenre_repo import get_genres_by_movie

def fetch_genres_for_movie(movie_id):
    return get_genres_by_movie(movie_id)
