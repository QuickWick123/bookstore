from django.urls import path
from . import views

urlpatterns = [
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/d/<int:book_id>', views.delete, name='delete'),
    path('wishlist/d2/<int:book_id>', views.deleteItem2, name='deleteItem2'),
    path('wishlist/d3/<int:book_id>', views.deleteItem3, name='deleteItem3'),
    path('wishlist/m1to2/<int:book_id>', views.moveItem1to2, name='moveItem1to2'),
    path('wishlist/m1to3/<int:book_id>', views.moveItem1to3, name='moveItem1to3'),
    path('wishlist/m2to1/<int:book_id>', views.moveItem2to1, name='moveItem2to1'),
    path('wishlist/m2to3/<int:book_id>', views.moveItem2to3, name='moveItem2to3'),
    path('wishlist/m3to1/<int:book_id>', views.moveItem3to1, name='moveItem3to1'),
    path('wishlist/m3to2/<int:book_id>', views.moveItem3to2, name='moveItem3to2'),
    path('wishlist/a2w1/<int:book_id>', views.add2wish1, name='add2wish1'),
    path('wishlist/add/', views.add, name='add'),
    path('wishlist/a2w2/<int:book_id>', views.add2wish2, name='add2wish2'),
    path('wishlist/a2w3/<int:book_id>', views.add2wish3, name='add2wish3'),
    path('wishlist/a/<int:book_id>', views.addCart, name='addCart'),
    path('wishlist/a2/<int:book_id>', views.addCart2, name='addCart2'),
    path('wishlist/a3/<int:book_id>', views.addCart3, name='addCart3'),
]
