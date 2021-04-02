from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='books-view'),
    path('ab/<int:book_id>', views.addCartB, name='addCartB'),
   # path('/<int:id>/', views.perBookView, name='books-view2'),
    #path('', views.render, name='template'),
]

