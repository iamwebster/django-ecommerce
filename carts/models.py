from django.db import models
from django.contrib.auth import get_user_model
from goods.models import ProductItem


class CartQuerySet(models.QuerySet):

    def total_price(self):
        return round(sum(cart.product_price() for cart in self), 2)
    
    def total_qty(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class UserCart(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = CartQuerySet().as_manager()

    def product_price(self):
        return round(self.product_item.product.sell_price() * int(self.quantity), 2)

    def __str__(self):
        return f"{self.user.username}'s cart | {self.product_item.product.name} | qty: {self.quantity}"