from django.db import models
from django.urls import reverse


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=(
        ('men', 'Men'),
        ('women', 'Women'),
    ))
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        self.image.name = f'{self.gender}/{self.name}/{self.image.name}'
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.gender} | {self.name}'


class ProductColor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
 

class Product(models.Model):
    class Meta:
        ordering = ('id',)

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL', blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='sneakers/')
    price = models.FloatField(default=0.00)
    discount = models.IntegerField(null=True, blank=True, verbose_name='Discount %')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.ManyToManyField(ProductColor)


    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price
    

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"product_slug": self.slug})
    

    def article(self):
        return f'{self.id:05}'


    def __str__(self):
        return self.name
    

class ProductShots(models.Model):
    class Meta:
        verbose_name_plural = 'Product shots'

    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    image1 = models.ImageField()
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)


    def save(self, *args, **kwargs):
        for i in range(1, 5):
            image_field = getattr(self, f"image{i}")
            if image_field:
                image_field.name = f"sneakers/{self.product.name}/{image_field.name}"
        super(ProductShots, self).save(*args, **kwargs)


    def __str__(self):
        return self.product.name
    

class ProductItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.DecimalField(default=00.0, max_digits=3, decimal_places=1)
    remains = models.PositiveIntegerField()

    
    def __str__(self):
        return f'{self.product.name} | {self.size}'