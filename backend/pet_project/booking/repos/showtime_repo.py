# booking/repos/showtime_repo.py
from booking.models.showtimes import Showtimes
from datetime import date
from django.db.models.functions import TruncDate
from collections import defaultdict
from django.utils.timezone import localdate
from datetime import datetime, timedelta

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
        
    def get_showtimes_grouped_by_date():
        now = datetime.now()
        seven_days_later = now + timedelta(days=7)

        showtimes = (
            Showtimes.objects
            .select_related("movie", "room")
            .annotate(date=TruncDate("start_time"))
            .filter(start_time__gte=now, start_time__lte=seven_days_later)
            .order_by("start_time")
        )

        result = defaultdict(lambda: defaultdict(lambda: {
            "movie_id": None,
            "title": "",
            "movie_poster_url": "",
            "duration": 0,
            "trailer_url": " ",
            "showtimes": []
        }))

        for s in showtimes:
            date_str = s.start_time.date().isoformat()
            movie_id = s.movie.id
            if result[date_str][movie_id]["movie_id"] is None:
                result[date_str][movie_id].update({
                    "movie_id": s.movie.id,
                    "title": s.movie.title,
                    "movie_poster_url": s.movie.movie_poster_url,
                    "duration": s.movie.duration,
                    "trailer_url": s.movie.trailer_url,
                })
            result[date_str][movie_id]["showtimes"].append({
                "id": s.id,
                "start_time": s.start_time,
                "room_name": s.room.room_name
            })

        final_result = []
        for date, movie_dict in result.items():
            final_result.append({
                "date": date,
                "movies": list(movie_dict.values())
            })

        return final_result