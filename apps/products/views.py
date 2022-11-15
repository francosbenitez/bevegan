from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
import json
from apps.accounts.forms import ContactoForm
from django.contrib import messages
from apps.products.models import Product
from apps.products.models import Request
from django.core import serializers

from apps.products.forms import RequestForm


# Create your views here.

def read_json():
    # with open("MOCK_DATA.json") as f:
    #     data = json.load(f)
    data = json.load(open('MOCK_DATA.json', encoding="utf8"))
    return data


def all_products(request):
    if request.method == "GET":
        # data = read_json()
        # Cambiar el data por la llamada a la base de datos
        data = Product.objects.all().values()

        return JsonResponse({"result": list(data)})
    else:
        return HttpResponse('All products')


def product_by_name(request, name):
    # data = read_json()
    # for key in data:
    #     if key["name"] == name:
    #         result.append(key)
    #
    data = Product.objects.filter(name=name).values()
    #result.append(data)
    return JsonResponse({"result": list(data)})


def product_by_category(request, category):
    # data = read_json()
    # result = []
    # for key in data:
    #     if key["category"] == category:
    #         result.append(key)
    # return JsonResponse({"result": result})

    result = Product.objects.filter(category__name=category).values()
    return JsonResponse({"result": list(result)})


def product_by_brand(request, brand):
    # data = read_json()
    # result = []
    # for key in data:
    #     if key["brand"] == brand:
    #         result.append(key)
    # return JsonResponse({"result": result})
    result = Product.objects.filter(brand__name=brand).values()
    return JsonResponse({"result": list(result)})


def product_by_id(request, id_product):
    # data = read_json()
    # result = []
    # for key in data:
    #     if key["id"] == id_product:
    #         result.append(key)
    # return JsonResponse({"result": result})
    result = Product.objects.filter(pk=id_product).values()
    return JsonResponse({"result": list(result)})


def form_request(request):
    if request.method == 'POST':
        # formulario = CategoriaForm(request.POST)
        formulario = RequestForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            # nombre = formulario.cleaned_data["nombre"]
            # nueva_categoria = Categoria(nombre=nombre)
            # nueva_categoria.save()
            return redirect('all_request')
    else:
        formulario = RequestForm()
    return render(request, 'products/add_request.html', {
        "formulario": formulario
    })


def all_request(request):
    data = Request.objects.all()
    #result.append(data)
    return render(request, 'products/all_request.html',{
        'requests': data
    })
