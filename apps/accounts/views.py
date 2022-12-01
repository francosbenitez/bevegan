from django.shortcuts import render, redirect
from django.http import HttpResponse
# from apps.accounts.forms import ContactoForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.views.generic import CreateView
from .forms import registerUser
from apps.accounts.models import Account, UserManager
from django.urls import reverse_lazy

# Create your view-s here.


# Create your views here.
def signup(request):
    if request.method == "GET":
        return render(request, "accounts/signup.html")
    else:
        if request.POST["password"] == request.POST["confirm_password"]:
            try:
                # registrer user
                user = User.objects.create_user(
                    username=request.POST["username"], password=request.POST["password"]
                )
                user.save()
                return HttpResponse("User created succesfully")
            except:
                return render(
                    request,
                    "accounts/signup.html",
                    {"error": "Username already exists"},
                )
        else:
            return render(
                request, "accounts/signup.html", {"error": "Password do not match"}
            )


def login(request):

    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        # TODO: buscar en la base de datos el email y el password
        if email != "juan@gmail.com":
            messages.error(request, "Email or password no exist")
        else:
            return render(
                request, "accounts/index.html", {"email": email, "password": password}
            )
    return render(request, "accounts/login.html")


def signup_form(request):
    message = None
    if request.method == "POST":
        contacto_form = ContactoForm(request.POST)
        if contacto_form.is_valid():
            message = "Create account successfully"
        else:
            message = "Error"
    else:
        contacto_form = ContactoForm()

    return render(
        request,
        "accounts/signup.html",
        {
            "title": "Sing up - beVegan",
            "contacto_form": contacto_form,
            "message": message,
        },
    )
