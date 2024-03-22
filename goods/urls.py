from django.urls import path 
from . import views 


urlpatterns = [
    path('', views.get_catalog, name='catalog'),
    path('all', views.get_products, name='all_products'),
    path('search/', views.get_search, name='search')
]