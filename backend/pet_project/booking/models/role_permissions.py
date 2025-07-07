from django.db import models
from booking.models.permissions import Permissions

class RolePermissions(models.Model):
    role = models.OneToOneField('Roles', models.DO_NOTHING, primary_key=True)  # The composite primary key (role_id, permission_id) found, that is not supported. The first column is selected.
    permission = models.ForeignKey(Permissions, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'role_permissions'
        unique_together = (('role', 'permission'),)