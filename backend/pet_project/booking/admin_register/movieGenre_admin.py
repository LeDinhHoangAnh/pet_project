from django.contrib import admin
from booking.models.movies_genres import MoviesGenres  # Đảm bảo đúng đường dẫn

@admin.register(MoviesGenres)
class MoviesGenresAdmin(admin.ModelAdmin):
    list_display = ('movie', 'genre', 'create_at', 'update_at')
    search_fields = ('movie__title', 'genre__genre_name')
    list_filter = ('genre',)
    ordering = ('-create_at',)
    readonly_fields = ('create_at', 'update_at')

    fieldsets = (
        (None, {
            'fields': ('movie', 'genre')
        }),
        ('Thông tin hệ thống', {
            'fields': ('create_at', 'update_at'),
            'classes': ('collapse',),
        }),
    )
