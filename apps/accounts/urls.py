from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    # path('index/', views.signup_form, name="other"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.signin, name="login"),
    path('logout/', views.signout, name="logout")
]
