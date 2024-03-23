from django.db import models


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
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='sneakers/')
    price = models.FloatField(default=0.00)
    discount = models.IntegerField(null=True, blank=True)
    quantity = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)


    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)


    def article(self):
        return f'{self.id:05}'


    def __str__(self):
        return self.name