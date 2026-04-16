from pprint import pprint

from django.core.cache import cache

from catalog.models import Product, Category
from config.settings import CACHE_ENABLED


def get_products_from_cache():
    """Получение данных о продуктах из кеша, если кеш пуст, получает данные из БД"""
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


def get_products_by_category(category_id):
    """Получение данных о продуктах в категории из кеша, если кеш пуст, получает данные из БД"""
    if not CACHE_ENABLED:
        return Product.objects.filter(category_id=category_id, is_publish=True)
    key = f"product_category_{category_id}"
    products = cache.get(key)
    if products is not None:
        return Product.objects.filter(category_id=category_id, is_publish=True)
    products = Product.objects.filter(category_id=category_id, is_publish=True)
    cache.set(key, products)
    return products


# def categories(request):
#         return {'categories': Category.objects.all()}
