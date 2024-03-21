from django.urls import path 
from . import views 


urlpatterns = [
    path('', views.get_catalog, name='catalog'),
    path('search/', views.get_search, name='search')
]