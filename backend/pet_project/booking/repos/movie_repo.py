from booking.models.movies import Movies

class MovieRepo:
    @staticmethod
    def get_all():
        return Movies.objects.all().order_by('-release_date')

    @staticmethod
    def get_by_id(movie_id):
        return Movies.objects.get(pk=movie_id)

    @staticmethod
    def create(data):
        return Movies.objects.create(**data)

    @staticmethod
    def update(instance, data):
        for attr, value in data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    @staticmethod
    def delete(instance):
        instance.delete()
