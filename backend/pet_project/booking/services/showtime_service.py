# booking/services/showtime_service.py
from booking.repos.showtime_repo import ShowtimeRepository

class ShowtimeService:
    @staticmethod
    def get_showtimes_by_movie(movie_id):
        return ShowtimeRepository.get_by_movie(movie_id)    
    @staticmethod
    def fetch_showtime_detail(showtime_id):
        return ShowtimeRepository.get_showtime_detail(showtime_id)