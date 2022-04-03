from django.urls import path
from .views import (get_product_list, get_product_by_id, get_category_list, get_category_by_id)

urlpatterns = [
    path('products', get_product_list),
    path('products/<int:product_id>', get_product_by_id),
    path('categories', get_category_list),
    path('categories/<int:category_id>', get_category_by_id),
]
