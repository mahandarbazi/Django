from django.urls import path
from . import views
from .views import BookListAPIView
urlpatterns = [
    path("books/",views.books,name='books'),
    path("add/",views.add_book,name="add"),
    path("api/books/",BookListAPIView.as_view(),name='api-books')
]