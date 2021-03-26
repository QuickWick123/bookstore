from django.urls import path
from .views import WishlistListView, WishlistDetailView, WishlistCreateView
from . import views

urlpatterns = [
    #path('wishlist/', WishlistListView.as_view(), name='wishlist'),
    path('wishlist/<int:pk>/', WishlistDetailView.as_view(), name='wishlist-detail'),
    path('wishlist/new/', WishlistCreateView.as_view(), name='wishlist-create'),
    path('wishlist/', views.wishlist, name='wishlist'),
]
