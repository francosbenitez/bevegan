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
        widgets = {
            'username' : forms.TextInput(
                attrs={
                'class': 'form-control',
                'placeholder':'username'
            }),
            'email' : forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'email'
                }),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'name'
                }),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'last name'
                }),
            'phone': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder':'phone'
            }),
            'password': forms.PasswordInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Confirm password',
                    'id' : 'password2',
                    'required':'required'
                }
            )
    }
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % account)
    def not_empty(valor):
        if len(valor) == 0:
            raise ValidationError("El password no puede ser vacio")
