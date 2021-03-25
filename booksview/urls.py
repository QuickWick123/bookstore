from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='books-view'),
    #path('', views.render, name='template'),
]

