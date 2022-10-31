from django.db import models
from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     pass

class wishlist(models.Model):
    # user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='wishlist')
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    link = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
