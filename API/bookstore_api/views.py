from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def books_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials

    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        book_serializer = BookSerializer(data=data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse(book_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)