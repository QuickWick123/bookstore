from django.urls import path
from bookstore_api import views, users
 
urlpatterns = [ 
    path('book/', views.BookAPIView.as_view()),
    path('detail/<int:id>/', views.BookDetails.as_view()),
    path('generic/book/', views.GenericAPIView.as_view()),
    path('users/', users.UsersAPIView.as_view()),
    path('userdetail/<int:id>/', users.userDetails.as_view())
]