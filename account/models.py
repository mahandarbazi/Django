from django.db import models

class Auth(models.Model):
    name = models.CharField(max_length=12,unique=True)
    password = models.CharField(max_length=8)
