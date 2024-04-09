from django.urls import path 
from . import views 


urlpatterns = [
    path('<slug:gender>/', views.categories, name='categories'),
    path('sneakers/<str:gender>/<slug:category_slug>/', views.catalog, name='catalog'),
    path('sneaker/<slug:product_slug>/', views.product, name='product_detail'),
    path('search/', views.search, name='search'),
]