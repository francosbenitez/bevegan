from django.shortcuts import render, redirect
from django.http import HttpResponse
# from apps.accounts.forms import ContactoForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.views.generic import CreateView
from .forms import registerUser
from apps.accounts.models import Account, UserManager
from django.urls import reverse_lazy
from apps.products import urls
# Create your view-s here.


def index(request):
    if request.user.is_authenticated:
        print(f"Username --> {request.user.username}")
        username = request.user.username
    else:
        return render(request, 'home.html')
    return render(request, 'home.html', {
        'username': username
    })


def signin(request):
    # usuario test pass test
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, "Email or password no exist")
        else:
            login(request, user)
            return redirect("home")
    return render(request, 'accounts/login.html')


def signout(request):
    logout(request)
    return redirect("login")


def register(request, *args, **kwargs):
    user = request.user

    if user.is_authenticated:
        return HttpResponse("You are already authenticated as " + str(user.email))

    context = {}
    if request.POST:
        form = registerUser(request.POST)
        if request.POST['password'] == request.POST['password2']:
            if form.is_valid():
                user = form.save()
                user.set_password(user.password)
                user.save()
                # login(request, user)
                context = {
                    'name': request.POST['name'],
                    'last_name': request.POST['last_name'],
                }
                return render(request, 'accounts/succes_user.html', context)
                # return redirect('succes', context)
            else:
                context['registration_form'] = form
        else:
            return render(request, 'accounts/signup.html', {
                    'error': 'Password do not match',
                    'form' : form
                })
    else:
        form = registerUser()
        context['registration_form'] = form
    return render(request, 'accounts/signup.html', context)
    # return render(request, 'accounts/create_user.html', context)


def succes_register(request):
    return render(request, 'accounts/succes_user.html')
    # return render(request, 'accounts/succes_user.html')
