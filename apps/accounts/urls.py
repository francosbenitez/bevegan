from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup),
    path('signup/', views.signup),
    path('login/', views.login)
]