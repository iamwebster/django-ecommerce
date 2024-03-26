from django.contrib import admin
from .models import Category, Product, Gender

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name',]}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    

@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
