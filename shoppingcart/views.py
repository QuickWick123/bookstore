from django.shortcuts import render
from django.http import HttpResponse

def shoppingcart(request):
    return HttpResponse('<h1>shopping cart page </h1>')

