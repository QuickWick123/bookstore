from django.contrib.sites import requests
from django.shortcuts import render
from django.http import HttpResponse


def wishlist(request):

    return render(request, 'pages/wishlist.html',)
