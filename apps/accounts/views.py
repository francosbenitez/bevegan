from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

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