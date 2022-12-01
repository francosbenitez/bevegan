from apps.accounts.models import Account
from django import forms
from django.forms import ValidationError

class registerUser(forms.ModelForm): 
    
    password2 = forms.CharField(label = 'Confirm password', widget= forms.PasswordInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Confirm password',
            'id' : 'password2',
            'required':'required'
        }
    ))
    class Meta:
        model = Account
        fields = [ 'username', 'name', 'last_name', 'email', 'phone', 'password' ]

def not_empty(valor):
    if len(valor) == 0:
        raise ValidationError("El password no puede ser vacio")


class ContactoForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        error_messages={"required": "Por favor complete el username"},
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Username",
                "name": "username",
            }
        ),
    )
    email = forms.EmailField(
        max_length=50,
        error_messages={"required": "Por favor complete el email"},
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "email",
                "placeholder": "Ingrese email",
                "name": "email",
            }
        ),
    )
    password = forms.CharField(
        max_length=50,
        validators=(not_empty,),
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password",
                "name": "password",
                "type": "password",
            }
        ),
    )
    confirm_password = forms.CharField(
        max_length=50,
        validators=(not_empty,),
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password",
                "name": "password",
                "type": "password",
            }
        ),
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
        except Account.DoesNotExist:
            return username
        raise forms.ValidationError('Username "%s" is already in use.' % username)
# class registerUser(forms.ModelForm):

        if password != confirm_password:
            msg = "Los passwords no son iguales"
            self.add_error("password", msg)
