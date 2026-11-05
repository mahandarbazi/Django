from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teachers/',include('teachers.urls')),
    path('coupon/',include('coupon.urls')),
    path('cookie/',include('cookie.urls')),
    path('session/',include('sessiontutorial.urls')),
    path('authentication/',include('authentication.urls')),
    path('account/',include('account.urls')),
    path('library/',include('library.urls')),
    path('api-auth/',include("rest_framework.urls"))
]