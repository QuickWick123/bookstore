from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>home page (index) </h1>')
    ##return render(request, 'pages/index.html')
