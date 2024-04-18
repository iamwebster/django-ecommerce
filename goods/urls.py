from django.urls import path 
from . import views 


urlpatterns = [
    path('search/', views.search, name='search'),
    path('sneaker/<slug:product_slug>/', views.product, name='product_detail'),

    path('<slug:category_name>/<str:style_url>/', views.catalog, name='catalog'),
]