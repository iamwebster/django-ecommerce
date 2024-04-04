from django.contrib import admin
from .models import Category, Product, Gender, ProductItem, ProductColor
from django.utils.html import format_html

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name',]}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    list_display = ['get_image', 'name', 'gender', 'category', 'discount', 'sell_price']
    list_display_links = ['get_image', 'name']
    list_editable = ['discount',]
    search_fields = ['name', 'description']
    list_filter = ['discount', 'category']
    fields = [
        ('name', 'slug'),
        'description',
        'image',
        ('price', 'discount'),
        ('category', 'gender'),
    ]

    def get_image(self, obj):
        return format_html('<img src="{}" width="75px" />'.format(obj.image.url))
    
    get_image.short_description = 'Image'
    

@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}


@admin.register(ProductItem)
class ProductItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'size', 'remains']
    list_filter = ['size', 'remains']


admin.site.register(ProductColor)
