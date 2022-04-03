from django.forms import model_to_dict
from django.http import JsonResponse

from .models import Product, Category


def get_product_list(request):
    product_list = Product.objects.all()
    return JsonResponse({'data': [model_to_dict(product) for product in product_list]})


def get_product_by_id(request, product_id: int):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'data': str(e)})
    return JsonResponse(model_to_dict(product))


def get_category_list(request):
    category_list = Category.objects.all()
    return JsonResponse({'data': [model_to_dict(category) for category in category_list]})


def get_category_by_id(request, category_id: int):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'data': str(e)})
    return JsonResponse(model_to_dict(category))
