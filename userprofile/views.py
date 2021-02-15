from django.shortcuts import render
from django.http import HttpResponse

def userprofile(request):
    return render(request, 'pages/userprofile.html')

