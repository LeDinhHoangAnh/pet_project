from django.db import models

class Cinemas(models.Model):
    cinemas_name = models.CharField(max_length=100)
    cinemas_address = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)  
    update_at = models.DateTimeField(auto_now=True)  

    class Meta:
        managed = True
        db_table = 'cinemas'
        verbose_name = 'Cinema'

    def __str__(self):
        return f"{self.cinemas_name}"