from django.urls import path
from . import views

urlpatterns = [
    path('code/',views.coupon_form,name='coupon_form'),
    path('success/',views.success,name='success'),
]