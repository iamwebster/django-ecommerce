from django.urls import path 
from . import views 


urlpatterns = [
    path('search/', views.search, name='search'),
    path('sneaker/<slug:product_slug>/', views.product, name='product_detail'),
    path('<slug:gender>/', views.categories, name='categories'),
    path('<str:gender>/<slug:category_slug>/', views.catalog, name='catalog'),
]