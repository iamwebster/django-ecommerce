from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.forms import ValidationError

from carts.models import UserCart
from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem

from .forms import UserLoginForm, UserRegistrationForm, ProfileForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)

                if session_key:
                    UserCart.objects.filter(session_key=session_key).update(user=user)
                    
                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('logout'):
                    return HttpResponseRedirect(request.POST.get('next'))
                
                return HttpResponseRedirect(reverse('home'))
    else:
        form = UserLoginForm()
        
    return render(request, 'users/login.html', {'form': form})


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key
            
            user = form.instance
            auth.login(request, user)

            if session_key:
                UserCart.objects.filter(session_key=session_key).update(user=user)

            return HttpResponseRedirect(reverse('home'))
    else:
        form = UserRegistrationForm()

    return render(request, 'users/registration.html', {'form': form})


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required
def profile(request):
    orders = Order.objects.filter(user=request.user)

    return render(request, 'users/profile.html', {'orders': orders})


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = UserRegistrationForm(instance=request.user)

    return render(request, 'users/update_profile.html', {'form': form})


# @login_required
def user_cart(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = UserCart.objects.filter(user=user)

                    if cart_items.exists():
                        # Create order
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data['phone_number'],
                            need_delivery=form.cleaned_data['need_delivery'],
                            delivery_address=form.cleaned_data['delivery_address'],
                            payment_on_delivery=form.cleaned_data['payment_on_delivery'],
                        )
                        # Create ordering products
                        for cart_item in cart_items:
                            product_item=cart_item.product_item
                            name=cart_item.product_item.product.name
                            price=cart_item.product_item.product.sell_price()
                            quantity=cart_item.quantity


                            if product_item.remains < quantity:
                                raise ValidationError(f'There is not enough quantity of product {name} in the warehouse\
                                                       In stock - {product_item.remains}')

                            OrderItem.objects.create(
                                order=order,
                                product_item=product_item,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )
                            product_item.remains -= quantity
                            product_item.save()

                        # Clean the user's cart after creating order
                        cart_items.delete()

                        return redirect('profile')
            except ValidationError:
                return redirect('cart')
    else:
        if request.user.is_authenticated:
            initial = {
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                }
        else:
            initial = None

        form = CreateOrderForm(initial=initial)

    context = {
        'form': form,
        'orders': True,
    }
    return render(request, 'users/cart_page.html', context=context)
