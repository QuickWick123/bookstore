from django.conf.urls import url 
from bookstore_api import views 
 
urlpatterns = [ 
    url(r'^books$', views.books_list),
]