from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('l/<str:query>/', views.home, name='home'),
    path('shortener/', views.generate, name='generate'),
    path('dashboard/<str:pk>/', views.dashboard, name='dashboard'),
    path('dashboard/edit/<str:pk>/', views.edit, name='edit'),
]
