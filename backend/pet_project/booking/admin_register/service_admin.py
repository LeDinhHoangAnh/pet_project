from traceback import format_tb
from django.contrib import admin, messages
from django.urls import path
from booking.models.services import Services
from django.contrib.admin import widgets as admin_widgets
from django import forms
from django.utils import timezone
from django.core.files.storage import default_storage
from django.conf import settings
from django.utils.html import format_html
import os

class SericeAdminForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = '__all__'
        
    upload_image = forms.ImageField(
        required=False, label="Upload Poster Image (chọn để thay đổi ảnh)"
    )
    def save(self, commit=True):
        instance = super().save(commit=False)

        # Nếu người dùng upload ảnh mới
        uploaded_file = self.cleaned_data.get('upload_image')
        if uploaded_file:
            # Lưu file vào thư mục 'media/posters/'
            filename = default_storage.save(f'services/{uploaded_file.name}', uploaded_file)
            instance.service_image_url = f'{settings.MEDIA_URL}{filename}'

        if commit:
            instance.save()
        return instance


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    form = SericeAdminForm
    list_display = ('id', 'service_name', 'service_description', 'service_price','create_at', 'update_at','poster_preview')
    list_display_links = ('id', 'service_name')
    search_fields = ('service_name', 'service_description')
    list_filter = ('service_price', 'service_name')
    readonly_fields = ('create_at', 'update_at','poster_preview') 

    fieldsets = (
        (None, {
            'fields': (
                'service_name',
                'service_description',
                'service_price',
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
        if obj.service_image_url:
            return format_html(f'<img src="{obj.service_image_url}" width="200" style="margin-top:10px;" />')
        return "(No image)"
    poster_preview.short_description = "Hiện tại"