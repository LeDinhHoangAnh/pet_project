from django.db import models

class Services(models.Model):
    service_name = models.CharField(max_length=100)
    service_description = models.TextField(blank=True, null=True)
    service_price = models.IntegerField()
    service_image_url = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services'