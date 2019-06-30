from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create/', views.create_view, name='create'),
    path('update/<int:custom_pk>/', views.update_view, name='update'),
    path('detail/<int:custom_pk>/', views.detail_view, name='detail'),
    path('delete/<int:custom_pk>/', views.delete, name='delete'),
    path('', include('django.contrib.auth.urls')),
    path('join/', views.signup, name='join'),
    path('login/', views.signin, name='login'),
    path('signout/', views.logout, name='logout'),
]