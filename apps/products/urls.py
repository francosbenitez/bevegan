from django.urls import path
from . import views

urlpatterns = [
    path('all', views.all_products, name="all_products"),
    path('name/<str:name>', views.product_by_name, name='product_by_name'),
    path('id/<int:id_product>', views.product_by_id, name='product_by_id'),
    path('category/<str:category>', views.product_by_category, name='product_by_category'),
    path('brand/<str:brand>', views.product_by_brand, name='product_by_brand')

]