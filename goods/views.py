from django.shortcuts import render
from .models import Category, Product, ProductItem
from django.core.paginator import Paginator
from .utils import query_search


def categories(request, gender_slug):
    categories = Category.objects.all()
    return render(
        request,
        "goods/categories.html",
        {"categories": categories, "gender_slug": gender_slug},
    )


def catalog(request, gender_slug, category_slug):
    page = request.GET.get('page', 1)
    order_by = request.GET.get('order_by', None)

    if category_slug != "all":
        products = Product.objects.filter(
            gender__slug=gender_slug, category__slug=category_slug
        )
    else:
        products = Product.objects.filter(gender__slug=gender_slug)

    if order_by == 'price' or order_by == '-price':
        products = products.order_by(order_by)
    
    paginator = Paginator(products, 40)
    current_page = paginator.page(int(page))

    return render(
        request, "goods/catalog.html", {"products": current_page, 'slug': category_slug})


def product(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    product_item = ProductItem.objects.filter(product__slug=product_slug)
    return render(request, "goods/product.html", {"product": product, 'items': product_item})


def search(request):
    query = request.GET.get('q', None)
    if query:
        products = query_search(query)
    else:
        products = None
    return render(request, 'goods/search.html', {'products': products})