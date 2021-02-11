from django.shortcuts import render
from django.http import HttpResponse

def userprofile(request):
    return HttpResponse('<h1> User profile log in? page </h1>')

