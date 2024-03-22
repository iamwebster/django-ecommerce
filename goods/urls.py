from django.urls import path 
from . import views 


urlpatterns = [
    path('<slug:gender_slug>/', views.categories, name='categories'),
    path('<slug:gender_slug>/<slug:category_slug>/', views.catalog, name='catalog'),
    path('sneaker/<slug:product_slug>/', views.product, name='product')
]