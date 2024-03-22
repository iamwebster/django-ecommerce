from django.contrib import admin
from .models import Category, Product, Gender


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name',]}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    

admin.site.register(Category, CategoryAdmin)
admin.site.register(Gender)
