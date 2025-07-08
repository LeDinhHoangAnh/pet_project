from django.db import models
from django.core.validators import MinValueValidator

class Movies(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    duration = models.IntegerField(validators=[MinValueValidator(1)])
    age_rating = models.CharField(max_length=10, blank=True, null=True)
    trailer_url = models.TextField(blank=True, null=True)
    movie_poster_url = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)  
    update_at = models.DateTimeField(auto_now=True)  

    class Meta:
        managed = True
        db_table = 'movies'
        verbose_name = 'Movie'
        
    def __str__(self):
        return self.title
