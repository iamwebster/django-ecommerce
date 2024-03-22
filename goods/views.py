from django.shortcuts import render
from .models import Category, Product
from django.core.paginator import Paginator


def categories(request, gender_slug):
    categories = Category.objects.filter(gender__slug=gender_slug)
    return render(
        request,
        "goods/categories.html",
        {"categories": categories, "gender_slug": gender_slug},
    )


def catalog(request, gender_slug, category_slug):
    if category_slug == "all":
        products = Product.objects.filter(gender__slug=gender_slug)
        category_name = 'All products'
    else:
        products = Product.objects.filter(
            gender__slug=gender_slug, category__slug=category_slug
        )
        category = Category.objects.get(slug=category_slug)
        category_name = category.name
    
    return render(
        request,
        "goods/catalog.html",
        {"products": products, "slug": category_slug, 'category_name': category_name},
    )


def product(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    return render(request, "goods/product.html", {"product": product})
