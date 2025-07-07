from django.db import models
from booking.models.bookings import Bookings

class Payments(models.Model):
    booking = models.ForeignKey(Bookings, models.DO_NOTHING)
    method = models.CharField(max_length=50)
    amount = models.IntegerField()
    status = models.CharField(max_length=20, blank=True, null=True)
    payment_transaction_code = models.CharField(max_length=100, blank=True, null=True)
    paid_at = models.DateTimeField(blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'payments'