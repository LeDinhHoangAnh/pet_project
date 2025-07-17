# booking/services/showtime_service.py
from booking.repos.showtime_repo import ShowtimeRepository
from collections import defaultdict

class ShowtimeService:
    @staticmethod
    def get_showtimes_by_movie(movie_id):
        return ShowtimeRepository.get_by_movie(movie_id)    
    @staticmethod
    def fetch_showtime_detail(showtime_id):
        return ShowtimeRepository.get_showtime_detail(showtime_id)

    def get_showtimes_by_date():
        return ShowtimeRepository.get_showtimes_grouped_by_date()
