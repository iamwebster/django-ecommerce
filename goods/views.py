from django.shortcuts import render
from .models import Category, Product


def get_catalog(request):
    categories = Category.objects.all()
    return render(request, 'goods/categories.html', {"categories": categories})

def get_products(request):
    products = Product.objects.all()
    return render(request, 'goods/catalog.html', {"products": products})


def get_search(request):
    return render(request, 'goods/search.html')