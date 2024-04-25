from django.shortcuts import render
from goods.models import Product


def main_page(request):
    '''The view for the main page and getting the ten recently added products'''
    products = Product.objects.order_by('-id')[:10]
    return render(request, 'main/main_page.html', {'products': products})
    

def about(request):
    '''The view for the about page'''
    return render(request, 'main/about.html')
