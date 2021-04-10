from django.contrib import admin
from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.home, name='books-view'),
    path('', include('wishlist.urls')),
   # path('/<int:id>/', views.perBookView, name='books-view2'),
    #path('', views.render, name='template'),
]

