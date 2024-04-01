from django.contrib import admin
from .models import Category, Product, Gender, ProductItem, ProductColor

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name',]}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    

@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}


admin.site.register(ProductItem)
admin.site.register(ProductColor)
