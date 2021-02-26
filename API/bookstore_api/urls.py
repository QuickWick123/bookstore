
from django.urls import path
from .views import book_list, book_detail, BookAPIView, BookDetails, GenericAPIView


urlpatterns = [
    path('book/', BookAPIView.as_view()),
    path('detail/<int:id>/', BookDetails.as_view()),
    path('generic/book/', GenericAPIView.as_view()),
]