from django.shortcuts import render
from django.http import HttpResponse
import requests


def home(request):

    response = requests.get('http://localhost:8000/book/')
    book = response.json()
    book1 = book[3]
    return render(request, 'pages/booksview.html', {"book": book1})

#def home(request):
    #return render(request, 'pages/booksview.html')
