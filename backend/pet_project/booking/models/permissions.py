from django.db import models

class Permissions(models.Model):
    permission_name = models.CharField(unique=True, max_length=100)
    permission_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'permissions'
        verbose_name = 'Permission'
    def __str__(self):
        return f"{self.permission_name}"
    