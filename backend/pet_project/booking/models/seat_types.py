from django.db import models

class SeatTypes(models.Model):
    seat_type_name = models.CharField(unique=True, max_length=50)
    seat_type_description = models.TextField(blank=True, null=True)
    seat_type_color_code = models.CharField(max_length=10, blank=True, null=True)
    seat_type_status = models.CharField(max_length=20, blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'seat_types'