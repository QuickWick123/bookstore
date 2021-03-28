from django.urls import path
from bookstore_api import views
from bookstore_api import users

urlpatterns = [
    path('book/', views.BookAPIView.as_view()),
    path('detail/<int:id>/', views.BookDetails.as_view()),
    path('generic/book/<int:id>/', views.GenericAPIView.as_view()),
    path('users/', users.UsersAPIView.as_view()),
    path('userdetail/<int:id>/', users.userDetails.as_view()),
    path('usercart/<int:id>/', users.userCart.as_view(), name="usercart"),  # new class for user cart API
    path('userwish/<int:id>/', users.userWish.as_view(), name="userwish"),
]
