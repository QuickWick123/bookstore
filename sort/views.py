import requests
from django.shortcuts import render
from django.http import HttpResponse

def sort(request):
    response = requests.get('http://localhost:5000/books')
    book = response.json()
    book1 = book[1]
    return render(request, 'pages/sort.html', {"book": book1})