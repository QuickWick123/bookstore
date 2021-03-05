from django.urls import path
from bookstore_api import views
from .views import GenericAPIView
from .views import BookViewSet
from rest_framework.routers import DefaultRouter
from django.conf.urls import include

router = DefaultRouter()
router.register('book', BookViewSet, basename='book')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('book/', views.BookAPIView.as_view()),
    path('detail/<int:id>/', views.BookDetails.as_view()),
    path('generic/book/<int:id>/', views.GenericAPIView.as_view()),
    path('users/', users.UsersAPIView.as_view()),
    path('userdetail/<int:id>/', users.userDetails.as_view())
]