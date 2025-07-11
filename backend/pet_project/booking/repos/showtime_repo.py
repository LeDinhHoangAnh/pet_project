# booking/repos/showtime_repo.py
from booking.models.showtimes import Showtimes

class ShowtimeRepository:
    @staticmethod
    def get_by_movie(movie_id):
        return Showtimes.objects.filter(movie_id=movie_id).select_related('room')
    
    def get_showtime_detail(showtime_id):
        try:
            return (
                Showtimes.objects
                .select_related('movie', 'room__cinema')
                .get(id=showtime_id)
            )
        except Showtimes.DoesNotExist:
            return None