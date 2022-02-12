from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('article/<str:slug>/', views.article_detail, name="article_detail"),
    path('add_article/', views.add_article, name="add_article"),
    path('edit_article/<str:slug>/', views.update_article, name="update_article"),
    path('delete_article/<str:slug>/', views.delete_article, name="delete_article"),
    
    path('user/login/', views.user_login, name="user_login"),
    path('user/logout/', views.user_logout, name="user_logout"),
    path('user/register/', views.user_register, name="user_register"),
    path('user/resetpassword/', views.reset_password, name="reset_password"),
]