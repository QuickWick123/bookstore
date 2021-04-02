from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm

def userprofile(request):
    if request.method == 'POST':
         form = SignUpForm(request.POST)
         if form.is_valid():
             form.save()
             username = form.cleaned_data.get('username')
             messages.success(request, f'Account created for {username}!')
             return redirect('userprofile')
    else:
        form = SignUpForm()
    return render(request, 'pages/userprofile.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('userprofile')
    else:
        form = SignUpForm()
        return render(request, 'pages/userprofile.html', {'form': form})