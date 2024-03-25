from django.urls import path 
from . import views 


urlpatterns = [
    path('search/', views.search, name='search'),
    path('<slug:gender_slug>/', views.categories, name='categories'),
    path('sneaker/<slug:product_slug>/', views.product, name='product_detail'),
    path('<slug:gender_slug>/<slug:category_slug>/', views.catalog, name='catalog'),
]