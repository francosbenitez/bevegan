from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup),
    path('signup/', views.signup_form, name="signup"),
    path('login/', views.login,name="login")
]