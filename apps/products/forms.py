from django import forms
from django.forms import ValidationError
from .models import Request
from .models import Category
from .models import Brand


class RequestForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(
            attrs={
                'class': "form-select"
            })
    )
    brand = forms.ModelChoiceField(
        queryset=Brand.objects.all(),
        widget=forms.Select(
            attrs={
                'class': "form-select"
            })
    )

    class Meta:
        model = Request
        # fields = '__all__'
        # fields = ['nombre']
        exclude = ('date_creation',)
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Ingrese nombre',
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Ingrese descripcion',
                'class': 'form-control'
            }),
        }
