from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=20)
    class_number = models.IntegerField()
    