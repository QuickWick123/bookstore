from django.urls import path
from . import views

urlpatterns = [
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/d/<int:book_id>', views.deleteItem, name='deleteItem'),
    path('wishlist/d2/<int:book_id>', views.deleteItem2, name='deleteItem2'),
    path('wishlist/d3/<int:book_id>', views.deleteItem3, name='deleteItem3'),
    path('wishlist/add/', views.add, name='add'),
    path('wishlist/a/<int:book_id>', views.addCart, name='addCart'),
    path('wishlist/a2/<int:book_id>', views.addCart2, name='addCart2'),
    path('wishlist/a3/<int:book_id>', views.addCart3, name='addCart3'),


]
