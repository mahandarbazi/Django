from django.shortcuts import render,redirect
from .models import *
from .forms import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BookSerializer
from rest_framework import status
def books(request):
    books = Book.objects.all()
    return render(request,'library/books.html',{"books":books})
def add_book(request):
    book = BookForm()
    if request.method == "POST":
        book = BookForm(request.POST)
        if book.is_valid():
            cd = book.cleaned_data
            Book.objects.create(title=cd['title'],
                                pages=cd['pages'],
                                author=cd["author"],
                                published_year=cd["published_year"])
            return redirect("books")
    else:
        book = BookForm()
    return render(request,'library/add_book.html',{"book":book})
            
class BookListAPIView(APIView):
    def get(self,request):
        books = Book.objects.all()
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)