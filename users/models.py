from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# AbstractUser
# username
# first_name
# last_name
# email
# password
# groups
# user_permissions
# is_staff
# is_active
# is_superuser
# last_login
# date_joined

# AbstractBaseUser
# id
# password
# last_login
from orders.common import OrderStatus


class User(AbstractUser):
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def shipping_address(self):
        return self.shippingaddress_set.filter(default=True).first()

    def has_shipping_address(self):
        return self.shipping_address is not None

    def orders_completed(self):
        return self.order_set.filter(status=OrderStatus.COMPLETED).order_by('-id')

class Customer(User):
    class Meta:
        proxy = True

    def get_product(self):
        return []

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
