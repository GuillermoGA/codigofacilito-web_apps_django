from django.db import models
from django.db.models.base import ModelState
from django.utils.translation import deactivate

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)  # 123456.78
    created_at = models.DateTimeField(auto_now_add=True)