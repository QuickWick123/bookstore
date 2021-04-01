from django.urls import path
from . import views

urlpatterns = [
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/d/<int:book_id>', views.deleteItem, name='deleteItem2'),
    path('wishlist/add/', views.add, name='add'),
    path('wishlist/a/<int:book_id>', views.addCart, name='addCart'),
]
