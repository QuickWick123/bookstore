from django.shortcuts import render
from django.http import HttpResponse

def shoppingcart(request):
    return render(request, 'pages/shoppingcart.html')

