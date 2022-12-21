from tabnanny import verbose
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length = 50)
    slug = models.SlugField(max_length = 50)        # Url representation of the title field

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self) :
        return self.title           # Display Category_name(Food) instead of (Object 1) on /admin


class Product(models.Model):
    user = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    
    title = models.CharField(max_length = 50)
    slug = models.SlugField(max_length = 50)        # Url representation of the title field
    description = models.TextField(blank = True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='uploads/product_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title