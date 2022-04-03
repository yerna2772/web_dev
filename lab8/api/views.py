from django.forms import model_to_dict
from django.http import JsonResponse

from .models import Product, Category


def get_object_by_id(model, object_id: int):
    try:
        object_from_db = model.objects.get(id=object_id)
    except model.DoesNotExist as e:
        return JsonResponse({'data': str(e)})
    return JsonResponse(model_to_dict(object_from_db))


def get_product_list(request):
    product_list = Product.objects.all()
    return JsonResponse({'data': [model_to_dict(product) for product in product_list]})


def get_product_by_id(request, product_id: int):
    return get_object_by_id(model=Product, object_id=product_id)


def get_category_list(request):
    category_list = Category.objects.all()
    return JsonResponse({'data': [model_to_dict(category) for category in category_list]})


def get_category_by_id(request, category_id: int):
    return get_object_by_id(model=Category, object_id=category_id)
