from booking.repos.movie_repo import MovieRepo

class MovieService:
    @staticmethod
    def list_movies():
        return MovieRepo.get_all()

    @staticmethod
    def retrieve(movie_id):
        return MovieRepo.get_by_id(movie_id)

    @staticmethod
    def create(data):
        return MovieRepo.create(data)

    @staticmethod
    def update(movie_id, data):
        movie = MovieRepo.get_by_id(movie_id)
        return MovieRepo.update(movie, data)

    @staticmethod
    def delete(movie_id):
        movie = MovieRepo.get_by_id(movie_id)
        return MovieRepo.delete(movie)
