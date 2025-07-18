from django.db import models
from booking.models.roles import Roles

class Users(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    user_phone = models.CharField(max_length=10)
    user_address = models.CharField(max_length=255)
    password_hash = models.CharField(max_length=255)
    role = models.ForeignKey(Roles, models.DO_NOTHING)
    account_type = models.CharField(max_length=50, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)  
    update_at = models.DateTimeField(auto_now=True)  

    class Meta:
        managed = True
        db_table = 'users'
        verbose_name = 'User'
    def __str__(self):
        return f"{self.user_email} - {self.user_name}"