from django.db import models
from django.contrib.auth import get_user_model

from goods.models import ProductItem
    

class OrderQuerySet(models.QuerySet):

    def total_price(self):
        if self:
            return round(sum(order.order_price() for order in self), 2)
        return 0
    
    def total_qty(self):
        if self:
            return sum(order.orderitem_quantity() for order in self)
        return 0
    

class Order(models.Model):
    user = models.ForeignKey(
        get_user_model(), 
        on_delete=models.SET_DEFAULT, 
        default=None, 
        blank=True, 
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=20)
    need_delivery = models.BooleanField(default=False)
    delivery_address = models.TextField(null=True, blank=True)
    payment_on_delivery = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    status = models.CharField(
        max_length=50,
        default="In processing",
        choices=(
            ("in_processing", "In processing"),
            ("sent", "Sent"),
            ("delivered", "Delivered"),
            ("refused", "Refused"),
        )
    )
    objects = OrderQuerySet().as_manager()


    def order_price(self):
        return round(sum(item.product_price() for item in self.orderitem_set.all()), 2)
    
    def orderitem_quantity(self):
        return sum(item.quantity for item in self.orderitem_set.all())

    def __str__(self):
        return f"Order № {self.pk} | Customer {self.user.first_name} {self.user.last_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    product_item = models.ForeignKey(
        to=ProductItem,
        on_delete=models.SET_DEFAULT,
        null=True,
        default=None,
    )
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


    def product_price(self):
        return round(self.product_item.product.sell_price() * self.quantity, 2)

    def __str__(self):
        return f"Product {self.name} | Order № {self.order.pk}"
