from traceback import format_tb
from django.contrib import admin, messages
from django.urls import path
from booking.models.movies import Movies
from django.contrib.admin import widgets as admin_widgets
from django import forms
from django.utils import timezone
from django.core.files.storage import default_storage
from django.conf import settings
from django.utils.html import format_html
import os

class MovieAdminForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = '__all__'
        widgets = {
            'release_date': admin_widgets.AdminDateWidget(),  # lịch chọn ngày đẹp
        }
    upload_image = forms.ImageField(
        required=False, label="Upload Poster Image (chọn để thay đổi ảnh)"
    )

    def clean_release_date(self):
        release_date = self.cleaned_data.get('release_date')
        if release_date and release_date < timezone.now().date():
            raise forms.ValidationError("Ngày phát hành không được trong quá khứ.")
        return release_date
    def save(self, commit=True):
        instance = super().save(commit=False)

        # Nếu người dùng upload ảnh mới
        uploaded_file = self.cleaned_data.get('upload_image')
        if uploaded_file:
            # Lưu file vào thư mục 'media/posters/'
            filename = default_storage.save(f'posters/{uploaded_file.name}', uploaded_file)
            instance.movie_poster_url = f'{settings.MEDIA_URL}{filename}'

        if commit:
            instance.save()
        return instance


@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    form = MovieAdminForm
    list_display = ('id', 'title', 'release_date', 'duration', 'age_rating', 'create_at', 'update_at','poster_preview')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_filter = ('release_date', 'age_rating')
    ordering = ('-release_date',)
    date_hierarchy = 'release_date'
    readonly_fields = ('create_at', 'update_at','poster_preview') 

    fieldsets = (
        (None, {
            'fields': (
                'title',
                'description',
                'duration',
                'age_rating',
                'release_date',
                'trailer_url',
                'upload_image',
                'poster_preview', 
            )
        }),
        ('Thông tin hệ thống', {
            'fields': ('create_at', 'update_at'),
            'classes': ('collapse',)
        }),
    )

    def poster_preview(self, obj):
        if obj.movie_poster_url:
            return format_html(f'<img src="{obj.movie_poster_url}" width="200" style="margin-top:10px;" />')
        return "(No image)"
    poster_preview.short_description = "Hiện tại"