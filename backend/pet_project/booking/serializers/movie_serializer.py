from rest_framework import serializers
from booking.models.movies import Movies

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'
