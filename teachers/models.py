from django.db import models

class Teachers(models.Model):
    name = models.CharField(max_length=12)
    email = models.EmailField()
    phone_number = models.IntegerField(max_length=11,default='09')
    bio = models.TextField(max_length=128)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)