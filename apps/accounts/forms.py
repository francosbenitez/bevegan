from django import forms
from django.forms import ValidationError


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

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            msg = "Los passwords no son iguales"
            self.add_error("password", msg)
