from django.db import models

class Movies(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    duration = models.IntegerField()
    age_rating = models.CharField(max_length=10, blank=True, null=True)
    trailer_url = models.TextField(blank=True, null=True)
    movie_poster_url = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movies'
