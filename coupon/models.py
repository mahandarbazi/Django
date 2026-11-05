from django.db import models

# Create your models here.
class Coupon(models.Model):
    code = models.CharField()
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.code}"
