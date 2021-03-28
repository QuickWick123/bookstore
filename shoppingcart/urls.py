from django.urls import path
from . import views

urlpatterns = [
    path('', views.shoppingcart, name='shoppingcart'), 
    path('d/<int:book_id>', views.deleteItem, name='deleteItem'),
    path('mtc/<int:book_id>', views.laterToCart, name='moveToCart'),
    path('u/<int:book_id>', views.updateQuantity, name='updateQuantity'),
    path('dl/<int:book_id>', views.deleteLaterItem, name='deleteLater'),
    path('sl/<int:book_id>', views.saveLaterItem, name='saveLater')
]