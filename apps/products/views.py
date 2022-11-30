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

from apps.products.forms import RequestForm, ProductForm


# Create your views here.

def read_json():
    # with open("MOCK_DATA.json") as f:
    #     data = json.load(f)
    data = json.load(open('MOCK_DATA.json', encoding="utf8"))
    return data


"""
PRODUCTS
"""


def all_products(request):
    # if request.method == "GET":
    #     # data = read_json()
    #     # Cambiar el data por la llamada a la base de datos
    #     data = Product.objects.all().values()
    #
    #     return JsonResponse({"result": list(data)})
    # else:
    #     return HttpResponse('All products')

    data = Product.objects.all().order_by('id')
    # result.append(data)
    return render(request, 'products/all.html', {
        'products': data
    })


def product_by_name(request, name):
    # data = read_json()
    # for key in data:
    #     if key["name"] == name:
    #         result.append(key)
    #
    # data = Product.objects.filter(name=name).values()
    # result.append(data)
    # return JsonResponse({"result": list(data)})
    data = Product.objects.filter(name=name)
    return render(request, 'products/all.html', {
        'products': data
    })


def product_by_category(request, category):
    # data = read_json()
    # result = []
    # for key in data:
    #     if key["category"] == category:
    #         result.append(key)
    # return JsonResponse({"result": result})

    # result = Product.objects.filter(category__name=category).values()
    # return JsonResponse({"result": list(result)})
    result = Product.objects.filter(category__name=category)
    return render(request, 'products/all.html', {
        'products': result
    })


def product_by_brand(request, brand):
    # data = read_json()
    # result = []
    # for key in data:
    #     if key["brand"] == brand:
    #         result.append(key)
    # return JsonResponse({"result": result})
    # result = Product.objects.filter(brand__name=brand).values()
    # return JsonResponse({"result": list(result)})
    result = Product.objects.filter(brand__name=brand)
    return render(request, 'products/all.html', {
        'products': result
    })


def product_by_id(request, id_product):
    # data = read_json()
    # result = []
    # for key in data:
    #     if key["id"] == id_product:
    #         result.append(key)
    # return JsonResponse({"result": result})
    # result = Product.objects.filter(pk=id_product).values()
    # return JsonResponse({"result": list(result)})
    result = Product.objects.filter(pk=id_product)
    return render(request, 'products/all.html', {
        'products': result
    })


def form_product(request):
    if request.method == 'POST':
        # formulario = CategoriaForm(request.POST)
        formulario = ProductForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            # nombre = formulario.cleaned_data["nombre"]
            # nueva_categoria = Categoria(nombre=nombre)
            # nueva_categoria.save()
            return redirect('all_products')
    else:
        formulario = RequestForm()
    return render(request, 'products/add.html', {
        "formulario": formulario
    })


def add_product_by_request(request, id_request):
    result = Request.objects.get(pk=id_request)
    product = Product(name=result.name, description=result.description, image=result.image,
                      category=result.category, brand=result.brand)
    result.soft_delete()
    product.save()
    return redirect('all_products')


"""
    REQUESTS
"""


def form_request(request):
    if request.method == 'POST':
        # formulario = CategoriaForm(request.POST)
        formulario = RequestForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            # nombre = formulario.cleaned_data["nombre"]
            # nueva_categoria = Categoria(nombre=nombre)
            # nueva_categoria.save()
            return redirect('all_request')
    else:
        formulario = RequestForm()
    return render(request, 'products/requests/add_request.html', {
        "formulario": formulario
    })


def all_request(request):
    data = Request.objects.all()
    # result.append(data)
    return render(request, 'products/requests/all_request.html', {
        'requests': data
    })
