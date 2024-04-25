from django.db import models
from django.urls import reverse


class Category(models.Model):
    '''The model for category names'''
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Style(models.Model):
    '''The model for styles'''
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    url = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.category} | {self.name}'


class ProductColor(models.Model):
    '''The model for the colors of the products'''
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    '''The model for describing products'''
    class Meta:
        ordering = ('id',)

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL', blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='sneakers/')
    price = models.FloatField(default=0.00)
    discount = models.IntegerField(null=True, blank=True, verbose_name='Discount %')
    sell_price = models.FloatField(null=True, blank=True)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    color = models.ManyToManyField(ProductColor)


    @property
    def get_sell_price(self):
        '''The method for getting the current price of the product'''
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price


    def save(self, *args, **kwargs):
        '''Redefined save method for 
        setting the final product price and 
        setting the correct image path'''
        self.sell_price = self.get_sell_price

        if self.name not in self.image.name:
            self.image.name = f"{self.name}/{self.image.name}"

        super(Product, self).save(*args, **kwargs)
        

    def get_absolute_url(self):
        '''The method for getting product url path'''
        return reverse("product_detail", kwargs={"product_slug": self.slug})
    

    def article(self):
        '''The method for generate product article'''
        return f'{self.id:05}'


    def __str__(self):
        return self.name
    

class ProductShots(models.Model):
    '''The model for storing paths to additional images for products'''
    class Meta:
        verbose_name_plural = 'Product shots'

    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    image1 = models.ImageField()
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)


    def save(self, *args, **kwargs):
        '''Redefined save method for configuring image paths'''
        for i in range(1, 5):
            image_field = getattr(self, f"image{i}")
            
            if self.product.name not in image_field.name and image_field:
                image_field.name = f"sneakers/{self.product.name}/{image_field.name}"
        super(ProductShots, self).save(*args, **kwargs)


    def __str__(self):
        return self.product.name
    

class ProductItem(models.Model):
    '''The model for the sizes and residues of a particular product'''
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.DecimalField(default=00.0, max_digits=3, decimal_places=1)
    remains = models.PositiveIntegerField()

    
    def __str__(self):
        return f'{self.product.name} | {self.size}'
    