from django.urls import path
from .views import SearchResultsView, BrowseResultsView
from . import views

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='SearchResultsView'),
    path('browse/', BrowseResultsView.as_view(), name='BroweseResultsView'),
    path('searchView/', views.searchview, name= 'searchView'),
    path('category_java/', views.category_java, name= 'java')
   
  
]