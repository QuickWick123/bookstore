from django.urls import path
from . import views

urlpatterns = [
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/d/<int:book_id>', views.deleteItem, name='deleteItem'),

]
