from django.urls import path
from . import views

urlpatterns = [
    path('set/',views.set_session),
    path('get/',views.get_session),
    path('update/',views.update_session),
    path('delete',views.delete_session),
]