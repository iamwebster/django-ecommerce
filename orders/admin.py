from django.contrib import admin
from django.utils.html import format_html

from .models import Order, OrderItem


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    '''Settings for the OrderItem model'''
    list_display = ['get_image', '__str__', 'quantity']
    list_display_links = ['get_image', '__str__']

    @admin.display(description='Product Image')
    def get_image(self, obj):
        '''The method for getting product main image and displaying it'''
        if obj.product_item.product.image:
            return format_html('<img src="{}" width="75px" />'.format(obj.product_item.product.image.url))
        return 'No image'


class OrderItemInline(admin.TabularInline):
    '''Inline table for the OrderAdmin'''
    model = OrderItem
    exclude = ['price',]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    '''Settings for the Order model'''
    list_display = ['__str__', 'updated_at', 'get_status_display']
    search_fields = ['id', 'user', 'status']
    list_filter = ['user', 'status', 'need_delivery', 'payment_on_delivery', 'is_paid']

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = [
            'user',
            'phone_number', 
            'need_delivery', 
            'delivery_address', 
            'is_paid', 
            'payment_on_delivery', 
            'created_at',
            'updated_at'
        ]

        if request.user.groups.filter(name='Managers').exists():
            return readonly_fields
        else:
            return self.readonly_fields
    
    inlines = [OrderItemInline]
