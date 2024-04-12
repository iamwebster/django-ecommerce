from django.shortcuts import render
from goods.models import Product


def main_page(request):
    products = Product.objects.order_by('-id')[:10]
    return render(request, 'main/main_page.html', {'products': products})
    

def about(request):
    return render(request, 'main/about.html')