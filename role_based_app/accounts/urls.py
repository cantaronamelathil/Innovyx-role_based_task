# role_based_app/urls.py
from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    
    path('', views.user_login, name='login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('logout',views.user_logout, name='user_logout'),
]
