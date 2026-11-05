from django.contrib import admin
from .models import Coupon

# Register your models here.
admin.site.register(Coupon)

class AdminForm(admin.ModelAdmin):
    pass