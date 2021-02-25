import requests
from django.shortcuts import render
from django.http import HttpResponse

def sort(request):
    return render(request, 'pages/sort.html')