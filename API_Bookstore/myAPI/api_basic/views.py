from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Book
from .serializers import BookSerializer


def book_list(request):
    """
    List all code articles, or create a new Article.
    """
    if request.method == 'GET':
        articles = Book.objects.all()
        serializer = BookSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
