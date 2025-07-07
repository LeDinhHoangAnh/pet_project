from django.contrib import admin
from booking.models.movies import Movies  # Đường dẫn đến model

@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_date', 'duration')
    search_fields = ('title',)
    list_filter = ('release_date',)
