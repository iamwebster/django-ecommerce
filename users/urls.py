from django.urls import path 
from . import views 


urlpatterns = [
    path('registration/', views.registration, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.update_profile, name='update_profile'),
    path('cart/', views.user_cart, name='cart'),
]