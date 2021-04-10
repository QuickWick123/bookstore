from django.shortcuts import render
from django.http import HttpResponse
import requests
import json


# def home(request):

#     response = requests.get('http://localhost:8000/book/')
#     book = response.json()
#     book1 = book[3]
#     return render(request, 'pages/booksview.html', {"book": book1})


def home(request):

    return render(request, 'pages/booksview.html', {"book": BookForLoop()})


def BookForLoop():

    response = requests.get('http://localhost:8000/book/')
    book = response.json()

    i = 0
    for book1 in book:
        book1 = book[i]
        i += 1
    return book

    # def perBookView(request, id):
    # get book information using id
    # Book = Book.objects.filter(id=id)
    # return render(request, 'pages/booksview.html')
