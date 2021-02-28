from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def userprofile(request):
    return render(request, 'pages/userprofile.html')