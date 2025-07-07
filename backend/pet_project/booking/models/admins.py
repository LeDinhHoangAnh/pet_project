from django.db import models
from booking.models.roles import Roles

class Admins(models.Model):
    admin_name = models.CharField(max_length=100)
    admin_email = models.CharField(unique=True, max_length=100)
    admin_password_hash = models.CharField(max_length=255)
    role = models.ForeignKey('Roles', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'admins'