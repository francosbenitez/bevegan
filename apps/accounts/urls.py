from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    # path('index/', views.signup_form, name="other"),
    path('login/', views.signin, name="login"),
    path('logout/', views.signout, name="logout"),
    path('register/', views.register, name='register'),
    path('succes/', views.succes_register, name='succes')

]
