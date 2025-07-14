from django.db import models

class Services(models.Model):
    service_name = models.CharField(max_length=100)
    service_description = models.TextField(blank=True, null=True)
    service_price = models.IntegerField()
    service_image_url = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)  
    update_at = models.DateTimeField(auto_now=True)  

    class Meta:
        managed = True
        db_table = 'services'
        verbose_name = 'Service'

    def __str__(self):
        return f"{self.service_name}"