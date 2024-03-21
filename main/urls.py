from django.urls import path 
from . import views 


urlpatterns = [
    path('', views.main_page, name='home'),
    path('about/', views.about, name='about')
]