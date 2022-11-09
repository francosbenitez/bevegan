from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from apps.accounts.forms import ContactoForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

# Create your view-s here.
def index(request):
    if request.user.is_authenticated:
        print("User is logged in :)")
        print(f"Username --> {request.user.username}")
        username = request.user.username
    else:
        print("User is not logged in :(")
        return render(request, 'home.html')
    return render(request, 'home.html', {
        'username': username
    })
    
def signup(request):
    print('entro1')
    if request.method == 'GET':
        print('entro2')
        return render(request, 'accounts/signup.html')
    else:
        if request.POST['password'] == request.POST['confirm_password']:
            try:    
                print('entro3')
                #registrer user
                user = User.objects.create_user(
                    username=request.POST['username'], 
                    password=request.POST['password']
                )
                user.save()
                login(request, user)
                #deberia retornar una pantalla de usuario creado
                return redirect("home")
            except:
                print('entro4')
                return render(request, 'accounts/signup.html', {
                    'error': 'Username already exists'
                })
        else:
            return render(request, 'accounts/signup.html', {
                    'error': 'Password do not match'
                })


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # # TODO: buscar en la base de datos el email y el password
        user = authenticate(
            request, 
            username = request.POST['username'],
            password = request.POST['password']
            )
        print(user)
        if user is None:
            messages.error(request, "Email or password no exist")
        else:
            # usuario prueba1@prueba pass prueba1 
            login(request, user)
            return redirect("home")
    return render(request, 'accounts/login.html')


# def signup_form(request):
#     message = None
#     if request.method == 'POST':
#         contacto_form = ContactoForm(request.POST)
#         if contacto_form.is_valid():
#             message = "Create account successfully"
#         else:
#             message = "Error"
#     else:
#         contacto_form = ContactoForm()
#     return render(
#         request,
#         'accounts/signup.html',
#         {
#             'title': "Sing up - beVegan",

#             'message': message
#         }
#     )
def signout(request):
    logout(request)
    return redirect("login")