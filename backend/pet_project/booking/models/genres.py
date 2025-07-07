from django.db import models

class Genres(models.Model):
    genre_name = models.CharField(unique=True, max_length=255)
    create_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'genres'

