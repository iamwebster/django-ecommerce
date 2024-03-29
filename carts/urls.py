from django.urls import path 
from . import views 


urlpatterns = [
    path('cart_add/', views.cart_add, name='cart_add'),
    path('cart_change/<cart_id>/<str:operation>/', views.cart_change, name='cart_change'),
    path('cart_remove/<int:cart_id>/', views.cart_remove, name='cart_remove'),
]
