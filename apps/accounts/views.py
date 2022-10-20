from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from apps.accounts.forms import ContactoForm


# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request, 'accounts/signup.html')
    else:
        if request.POST['password'] == request.POST['confirm_password']:
            try:    
                #registrer user
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
                user.save()
                return HttpResponse('User created succesfully')
            except:
                return render(request, 'accounts/signup.html', {
                    'error': 'Username already exists'
                })
        else:
            return render(request, 'accounts/signup.html', {
                    'error': 'Password do not match'
                })


def login(request):
    return render(request, 'accounts/login.html')


def signup_form(request):
    message = None
    if request.method == 'POST':
        contacto_form = ContactoForm(request.POST)
        if contacto_form.is_valid():
            message = "Create account successfully"
        else:
            message = "Error"
    else:
        contacto_form = ContactoForm()

    return render(
        request,
        'accounts/signup.html',
        {
            'title': "Sing up - beVegan",
            'contacto_form': contacto_form,
            'message': message
        }
    )
