from django.shortcuts import render, redirect
from goods.models import Product 
from .models import UserCart


def cart_add(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.user.is_authenticated:
        cart = UserCart.objects.filter(user=request.user, product=product)

        if cart.exists():
            cart_item = cart.first()
            if cart_item:
                cart_item.quantity += 1
                cart_item.save()
        else:
            UserCart.objects.create(user=request.user, product=product, quantity=1)
    
    return redirect(request.META['HTTP_REFERER'])


def cart_change(request, product_id):
    pass 


def cart_remove(request, cart_id):
    
    cart = UserCart.objects.get(id=cart_id)
    cart.delete()
    return redirect(request.META['HTTP_REFERER'])