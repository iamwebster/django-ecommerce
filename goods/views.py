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
    page = request.GET.get('page', 1)

    if category_slug == "all":
        products = Product.objects.filter(gender__slug=gender_slug)
    else:
        products = Product.objects.filter(
            gender__slug=gender_slug, category__slug=category_slug
        )
    
    paginator = Paginator(products, 30)
    current_page = paginator.page(int(page))

    return render(
        request,
        "goods/catalog.html",
        {"products": current_page, "slug": category_slug},
    )


def product(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    return render(request, "goods/product.html", {"product": product})
