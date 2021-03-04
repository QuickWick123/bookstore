import requests
from django.shortcuts import render
from django.http import HttpResponse

def sort(request):
   #  return render(request, 'pages/sort.html')
    response = requests.get('http://localhost:5000/book')
    book = response.json()
    book1 = book[0]
    return render(request, 'pages/sort.html', {"book": book1})