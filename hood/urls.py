from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'indexPage'),  
    path('join_hood/', views.join_hood, name='join-hood'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_user, name='login'),
    path('signup/', views.signup, name='signup'),
]