from django.urls import path
from .views import SearchResultsView
from . import views

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='SearchResultsView')
]