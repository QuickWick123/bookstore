from django.urls import path
from . import views

urlpatterns = [
    path('', views.shoppingcart, name='shoppingcart'),
    path('d/<int:book_id>', views.deleteItem, name='deleteItem'),
    path('u/<int:book_id>', views.updateQuantity, name='updateQuantity')

]