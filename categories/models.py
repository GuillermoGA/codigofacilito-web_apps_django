from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH
from products.models import Product
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.title