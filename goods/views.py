from django.shortcuts import render, redirect
from django.core.paginator import Paginator
import math 

from .models import Product
from .utils import query_search


def catalog(request, category_name, style_url):
    '''The view for getting a products for catalog'''
    page = request.GET.get('page', 1)
    order_by = request.GET.get('order_by', 'id') 
    min_price_filter = request.GET.get('min_price', None)
    max_price_filter = request.GET.get('max_price', None)
    reset = request.GET.get('reset', None)  


    products = Product.objects.filter(style__category__name=category_name)

    if style_url != 'all':    
        products = Product.objects.filter(style__category__name=category_name, style__url=style_url)


    if products:
        prices_list = sorted(products.values_list('sell_price', flat=True))
        
        min_price = int(prices_list[0])
        max_price = math.ceil(prices_list[-1])


        if not min_price_filter or not max_price_filter or reset:
            min_price_filter = min_price
            max_price_filter = max_price


        products = products.filter(sell_price__gte=min_price_filter, sell_price__lte=max_price_filter).order_by(order_by)


    paginator = Paginator(products, 40)
    current_page = paginator.page(int(page))


    if reset:
        return redirect('catalog', category_name=category_name, style_url=style_url)


    return render(request, 'goods/catalog.html', {'products': current_page, 
                                                  'category_name': category_name, 
                                                  'style_url': style_url,
                                                  'order_by': order_by,
                                                  'min_price_filter': min_price_filter,
                                                  'max_price_filter': max_price_filter,
                                                   })


def product(request, product_slug):
    '''The view for a product detail page'''
    product = Product.objects.get(slug=product_slug)
    return render(request, "goods/product.html", {"product": product})


def search(request):
    '''The view for a products search'''
    query = request.GET.get('q', None)
    if query:
        products = query_search(query)
    else:
        products = None
    return render(request, 'goods/search.html', {'products': products})
