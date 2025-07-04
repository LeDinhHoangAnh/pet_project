from django.db import models

class Cinemas(models.Model):
    cinemas_name = models.CharField(max_length=100)
    cinemas_address = models.CharField(max_length=255)
    create_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cinemas'