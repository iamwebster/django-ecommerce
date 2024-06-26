from django.contrib import admin
from .models import Product, ProductItem, ProductColor, ProductShots, Style, Category
from django.utils.html import format_html
from django.utils.text import slugify


class ProductItemInline(admin.TabularInline):
    '''Inline table for the ProductAdmin'''
    model = ProductItem
    extra = 5


class ProductShotsInline(admin.StackedInline):
    '''Inline table for the ProductAdmin'''
    model = ProductShots


@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    '''Settings for the Style model'''
    prepopulated_fields = {'url': ['name',]}
    list_display = ['name', 'category', 'url']
    list_display_links = ['name',]
    list_filter = ['name', 'category']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''Settings for the Product model'''
    prepopulated_fields = {'slug': ['name', 'color']}
    list_display = ['get_image', 'name', 'color_name', 'style', 'discount', 'sell_price']
    list_display_links = ['get_image', 'name']
    list_editable = ['discount',]
    search_fields = ['name', 'description']
    list_filter = ['discount', 'style']
    readonly_fields = ['sell_price',]
    fields = [
        ('name', 'slug'),
        'description',
        'image',
        'color',
        ('price', 'discount', 'sell_price'),
        'style',
    ]
    inlines = [ProductItemInline, ProductShotsInline]
    save_on_top = True

    def color_name(self, obj):
        '''The method for getting the names of colors and displaying them in the list_display'''
        return slugify([i.name for i in obj.color.all()])
        
    @admin.display(description='Product Image')
    def get_image(self, obj):
        '''The method for getting product main image and displaying it'''
        if obj.image:
            return format_html('<img src="{}" width="75px" />'.format(obj.image.url))
        return 'No image'
    
    

@admin.register(ProductItem)
class ProductItemAdmin(admin.ModelAdmin):
    '''Settings for the ProductItem model'''
    list_display = ['product', 'size', 'remains']
    list_filter = ['size', 'remains']


admin.site.register(ProductShots)
admin.site.register(ProductColor)
admin.site.register(Category)
