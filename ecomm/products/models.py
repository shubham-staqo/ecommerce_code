from distutils.command.upload import upload
from enum import unique
from pyexpat import model
from re import U
from django.db import models
from base.models import Basemodel


class Category(Basemodel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=False)
    category_image = models.ImageField(upload_to="categories")




class Product(Basemodel):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True , blank=False)
    category = models.ForeignKey(Category , on_delete=models.CASCADE, related_name="products")
    price = models.IntegerField()
    product_description = models.TextField()




class ProductImage(Basemodel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")
    image = models.ImageField(upload_to = product)



