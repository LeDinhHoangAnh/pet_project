from django.contrib import admin
from booking.models.genres import Genres 

@admin.register(Genres)
class GenresAdmin(admin.ModelAdmin):
    list_display = ('id', 'genre_name', 'create_at', 'update_at')
    search_fields = ('genre_name',)
    ordering = ('-create_at',)
    list_per_page = 25
    readonly_fields = ('create_at', 'update_at')

    fieldsets = (
        (None, {
            'fields': ('genre_name',)
        }),
        ('Thông tin hệ thống', {
            'fields': ('create_at', 'update_at'),
            'classes': ('collapse',),
        }),
    )
