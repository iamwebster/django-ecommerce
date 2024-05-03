from django.contrib import admin
from django.utils.html import format_html

from .models import Order, OrderItem


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    '''Settings for the OrderItem model'''
    list_display = ['get_image', '__str__', 'product_item', 'quantity']
    list_display_links = ['get_image', '__str__']
    search_fields = ['name',]
    list_filter = ['order', 'quantity']
    readonly_fields = ['get_image',]
    fields = [
        'get_image',
        'order',
        'product_item',
        'name',
        'price',
        'quantity',
    ]

    @admin.display(description='Product Image')
    def get_image(self, obj):
        '''The method for getting product main image and displaying it'''
        if obj.product_item.product.image:
            return format_html('<img src="{}" width="75px" />'.format(obj.product_item.product.image.url))
        return 'No image'


class OrderItemInline(admin.StackedInline):
    '''Inline table for the OrderAdmin'''
    model = OrderItem
    show_change_link = True
    exclude = ['price',]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    '''Settings for the Order model'''
    list_display = ['__str__', 'updated_at', 'get_status_display']
    search_fields = ['id', 'user', 'status']
    list_filter = ['user', 'status', 'need_delivery', 'payment_on_delivery', 'is_paid']
    inlines = [OrderItemInline]

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
    