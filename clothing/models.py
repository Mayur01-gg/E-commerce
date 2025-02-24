from django.db import models

# Create your models here.

class Product(models.Model):
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Extra Extra Large'),
    ]
    COLOR_CHOICES = [
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Black', 'Black'),
        ('White', 'White'),
        ('Brown', 'Brown'),
        ('Default', 'Default')
    ]

    name = models.CharField(max_length=200)
    size = models.CharField(max_length=3, choices=SIZE_CHOICES, default='M')
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='Black')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_img/')

    def __str__(self):
        return self.name        