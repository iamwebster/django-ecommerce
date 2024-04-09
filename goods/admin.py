from django.contrib import admin
from .models import Category, Product, ProductItem, ProductColor, ProductShots
from django.utils.html import format_html

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['gender', 'name']}
    list_display = ['name', 'gender', 'slug']
    list_filter = ['name', 'gender']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    list_display = ['get_image', 'name', 'category', 'discount', 'sell_price']
    list_display_links = ['get_image', 'name']
    list_editable = ['discount',]
    search_fields = ['name', 'description']
    list_filter = ['discount', 'category']
    fields = [
        ('name', 'slug'),
        'description',
        'image',
        ('price', 'discount'),
        ('category'),
    ]

    def get_image(self, obj):
        return format_html('<img src="{}" width="75px" />'.format(obj.image.url))
    
    get_image.short_description = 'Image'
    

@admin.register(ProductItem)
class ProductItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'size', 'remains']
    list_filter = ['size', 'remains']


admin.site.register(ProductColor)
admin.site.register(ProductShots)
