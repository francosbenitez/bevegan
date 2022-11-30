from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Products
    path("all", views.all_products, name="all_products"),
    path("name/<str:name>", views.product_by_name, name="product_by_name"),
    path("id/<int:id_product>", views.product_by_id, name="product_by_id"),
    path(
        "category/<str:category>", views.product_by_category, name="product_by_category"
    ),
    path("brand/<str:brand>", views.product_by_brand, name="product_by_brand"),
    path("add", views.form_product, name="add_product"),
    # Request
    path("add/request", views.form_request, name="add_request"),
    path("all/request", views.all_request, name="all_request"),
    path(
        "add/product/<int:id_request>",
        views.add_product_by_request,
        name="add_product_by_request",
    ),
]
