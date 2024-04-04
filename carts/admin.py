from django.contrib import admin

from .models import UserCart


@admin.register(UserCart)
class UserCartAdmin(admin.ModelAdmin):
    list_display = ['user_display', 'product_item', 'quantity']
    list_filter = ['user',]

    def user_display(self, obj):
        if obj.user:
            return str(obj.user.username)
        return 'Anonymous user'
    
    user_display.short_description = 'User'