from django.contrib import admin
from .models import Product, ProductItem, ProductColor, ProductShots, Style, Category
from django.utils.html import format_html
from django.utils.text import slugify


@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ['name',]}
    list_display = ['name', 'category', 'url']
    list_display_links = ['name',]
    list_filter = ['name', 'category']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name', 'color']}
    list_display = ['get_image', 'name', 'color_name', 'style', 'discount', 'sell_price']
    list_display_links = ['get_image', 'name']
    list_editable = ['discount',]
    search_fields = ['name', 'description']
    list_filter = ['discount', 'style']
    fields = [
        ('name', 'slug'),
        'description',
        'image',
        'color',
        ('price', 'discount'),
        ('style'),
    ]

    
    def color_name(self, obj):
        return slugify([i.name for i in obj.color.all()])
        

    def get_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="75px" />'.format(obj.image.url))
        return 'No image'
    
    get_image.short_description = 'Image'
    

@admin.register(ProductItem)
class ProductItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'size', 'remains']
    list_filter = ['size', 'remains']


admin.site.register(ProductShots)
admin.site.register(ProductColor)
admin.site.register(Category)
