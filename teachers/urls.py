from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.add_teacher,name="add"),
    path('list/',views.teachers_list,name = 'teachers_list'),
    path('update/<int:id>/',views.update_teachers,name = 'update'),
    path('delete/<int:id>/',views.delete_teacher,name='delete'),
]