from . import views
from django.conf.urls import url, include
from django.urls import path
 
urlpatterns = [
    url(r'^$', views.index, name='home'),
    path('signup/', views.signup, name='signup'), #added
]