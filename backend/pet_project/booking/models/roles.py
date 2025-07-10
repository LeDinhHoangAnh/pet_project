from django.db import models

class Roles(models.Model):
    role_name = models.CharField(unique=True, max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)  
    update_at = models.DateTimeField(auto_now=True)  

    class Meta:
        managed = True
        db_table = 'roles'
        verbose_name = "Role"
    def __str__(self):
        return f"{self.role_name}"