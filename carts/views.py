from django.shortcuts import render, redirect
from django.http import JsonResponse
from goods.models import Product, ProductItem
from .models import UserCart


def cart_add(request):
    product_id = request.POST.get("product_id")
    size = request.POST.get('size')
    product = Product.objects.get(id=product_id)

    product_item = product.productitem_set.get(size=size)
    if request.user.is_authenticated:
        cart = UserCart.objects.filter(user=request.user, product_item=product_item)

        if cart.exists():
            cart_item = cart.first()
            if cart_item:
                cart_item.quantity += 1
                cart_item.save()
        else:
            UserCart.objects.create(user=request.user, product_item=product_item, quantity=1)
    
    return JsonResponse({'message': 'The product has been added to cart!'})


def cart_change(request):
    
    cart_id = request.POST.get("cart_id")
    quantity = request.POST.get("quantity")

    cart = UserCart.objects.get(id=cart_id)

    cart.quantity = quantity
    cart.save()
    updated_quantity = cart.quantity
    cart_price = cart.product_price()
    total_price = UserCart.objects.filter(user=request.user).total_price()
    response_data = {
        "message": "Products have been updated!",
        "quantity": updated_quantity,
        'total_price': total_price,
        'cart_price': cart_price,
    }

    return JsonResponse(response_data)


def cart_remove(request):
    cart_id = request.POST.get('cart_id')

    cart = UserCart.objects.get(id=cart_id)
    quantity = cart.quantity
    cart_price = cart.product_price()
    cart.delete()

    response_data = {
        'message': 'The product has been deleted!',
        'quantity_deleted': quantity,
        'cart_price': cart_price,
    }
    return JsonResponse(response_data)