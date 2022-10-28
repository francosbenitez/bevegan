from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
import json
from apps.accounts.forms import ContactoForm
from django.contrib import messages


# Create your views here.

def read_json():
    # with open("MOCK_DATA.json") as f:
    #     data = json.load(f)
    data = json.load(open('MOCK_DATA.json', encoding="utf8"))
    return data


def all_products(request):
    if request.method == "GET":
        data = read_json()
        #Cambiar el data por la llamada a la base de datos
        return JsonResponse({"result": data})
    else:
        return HttpResponse('All products')


def product_by_name(request, name):
    data = read_json()
    result = []
    for key in data:
        if key["name"] == name:
            result.append(key)
    return JsonResponse({"result": result})


def product_by_category(request, category):
    data = read_json()
    result = []
    for key in data:
        if key["category"] == category:
            result.append(key)
    return JsonResponse({"result": result})


def product_by_brand(request, brand):
    data = read_json()
    result = []
    for key in data:
        if key["brand"] == brand:
            result.append(key)
    return JsonResponse({"result": result})


def product_by_id(request, id_product):
    data = read_json()
    result = []
    for key in data:
        if key["id"] == id_product:
            result.append(key)
    return JsonResponse({"result": result})
