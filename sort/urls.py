from django.urls import path
from .views import SearchResultsView, browse_results_view, browse_by_category
from . import views

urlpatterns = [
    
    
    path(r'?P<catetgory>', views.browse_by_category, name='browse_by_category'),
    path(r'', views.browse_results_view, name='BroweseResultsView'),
    path('searchView/', views.searchview, name= 'searchView'),
    path('search/', SearchResultsView.as_view(), name='SearchResultsView')
  
]