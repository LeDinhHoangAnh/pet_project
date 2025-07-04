from django.db import models

class Roles(models.Model):
    role_name = models.CharField(unique=True, max_length=50)
    create_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'