from django.urls import path
from . import views

urlpatterns = [
    path('', views.userprofile, name='userprofile'),
    path('signup/', views.signup, name='signup'),
]
