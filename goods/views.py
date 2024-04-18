from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
from .utils import query_search


def catalog(request, category_name, style_url):
    page = request.GET.get('page', 1)

    style_filter = request.GET.get('style', None)
    if style_filter:
        style_url = style_filter

    order_by = request.GET.get('order_by', 'id') 

    if style_url != 'all':
        products = Product.objects.filter(style__url=style_url)
    else:
        products = Product.objects.filter(style__category__name=category_name)


    prices_list = Product.objects.values_list('price', flat=True)
    min_price = int(prices_list.order_by('price').first())
    max_price = int(prices_list.order_by('price').last())

    min_price_filter = request.GET.get('min_price', None)
    max_price_filter = request.GET.get('max_price', None)
    if not min_price_filter or not max_price_filter:
        min_price_filter = min_price
        max_price_filter = max_price
    
    
    products = products.filter(price__gte=min_price_filter, price__lte=max_price_filter).order_by(order_by)

    paginator = Paginator(products, 40)
    current_page = paginator.page(int(page))


    return render(request, 'goods/catalog.html', {'products': current_page, 
                                                  'category_name': category_name, 
                                                  'style_url': style_url,
                                                  'order_by': order_by,
                                                  'min_price_filter': min_price_filter,
                                                  'max_price_filter': max_price_filter,})


def product(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    return render(request, "goods/product.html", {"product": product})


def search(request):
    query = request.GET.get('q', None)
    if query:
        products = query_search(query)
    else:
        products = None
    return render(request, 'goods/search.html', {'products': products})