from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        user = self.create_user(username=username, email=email, password=password, **extra_fields)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.email

class Wishlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_wishlist')
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    link = models.CharField(max_length=500)
    image = models.CharField(max_length=500)

class Values(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='checked_values')
    checked = models.JSONField(encoder=None)

class Brand(models.Model):
    id = models.CharField(max_length=64, primary_key=True)
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=500)
    num_devices = models.IntegerField()

class Device(models.Model):
    id = models.CharField(max_length=64, primary_key=True)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand_device')
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=500)
    thumbnail = models.CharField(max_length=500)
    summary = models.CharField(max_length=500)

class Device_specification(models.Model):
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='device_device_specification')
    spec_id = models.IntegerField(primary_key=True)
    spec_category = models.CharField(max_length=64)
    specification = models.CharField(max_length=64)
    spec_value = models.CharField(max_length=64)



