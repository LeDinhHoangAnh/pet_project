# booking/repos/showtime_repo.py
from booking.models.showtimes import Showtimes

class ShowtimeRepository:
    @staticmethod
    def get_by_movie(movie_id):
        return Showtimes.objects.filter(movie_id=movie_id).select_related('room')
