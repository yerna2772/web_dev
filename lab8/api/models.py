from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name of product')
    price = models.FloatField(verbose_name='Price of product')
    description = models.TextField(verbose_name='Description of product')
    count = models.IntegerField(verbose_name='Count of product')
    is_active = models.BooleanField(verbose_name='Sign of activity of a product')

    def __str__(self):
        return f"{self.name}  -- {self.price}"


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name of the category')

    def __str__(self):
        return f"{self.name}"
