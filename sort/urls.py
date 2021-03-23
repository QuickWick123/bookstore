from django.urls import path, re_path
from .views import SearchResultsView, browse_results_view, browse_by_category, top_10_sellers, top_20_sellers, rating
from . import views

urlpatterns = [

    path(r'?P<catetgory>', views.browse_by_category, name='browse_by_category'),
    path(r'', views.browse_results_view, name='BroweseResultsView'),
    path(r'top10sellers', views.top_10_sellers, name='top_10_sellers'),
    path(r'top20sellers/', views.top_20_sellers, name='top_20_sellers'),
    re_path(r'^top20sellers/(?P<page>\d+)/', views.top_20_sellers, name='top_20_sellers'),
    path(r'rating', views.rating, name='rating'),
    path('searchView/', views.searchview, name= 'searchView'),
    path(r'search/', SearchResultsView.as_view(), name='SearchResultsView'),
    
  
]