from django.db import models
from django.utils.text import slugify


class Gender(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name 


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    class Meta:
        ordering = ('id',)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='sneakers/')
    price = models.FloatField(default=0.00)
    discount = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)


    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price


    def article(self):
        return f'{self.id:05}'


    def __str__(self):
        return self.name
    

class ProductColor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class ProductSize(models.Model):
    size = models.DecimalField(default=00.0, max_digits=3, decimal_places=1)
    remains = models.PositiveIntegerField()
    

class ProductItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.DecimalField(default=00.0, max_digits=3, decimal_places=1)
    remains = models.PositiveIntegerField()

    
    def __str__(self):
        return f'{self.product.name} | {self.size} | {self.remains}'