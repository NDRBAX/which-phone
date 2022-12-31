from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username,password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,**extra_fields)
        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, username, email,password=None, **extra_fields):
        user = self.create_user(username=username, email=email, password=password, **extra_fields)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    avatar_url = models.URLField(blank=True, null=True, default="https://cdn-icons-png.flaticon.com/512/3177/3177440.png")
    wishlist = models.ManyToManyField('Device', related_name='wishlist_users', blank=True)
    secure_question = models.CharField(max_length=255, blank=True, null=True)
    secure_answer = models.CharField(max_length=255 , blank=True, null=True)
    history = models.ManyToManyField('Specification', related_name='history_users', blank=True)
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



class Specification(models.Model):
    battery = models.CharField(max_length=64)
    ram = models.CharField(max_length=64)
    storage = models.CharField(max_length=64)
    chipset = models.CharField(max_length=64)
    screen_size = models.CharField(max_length=64)
    screen_resolution = models.CharField(max_length=64)
    rear_camera = models.CharField(max_length=64)
    rear_camera_video = models.CharField(max_length=64)
    front_camera = models.CharField(max_length=64)
    front_camera_video = models.CharField(max_length=64)
    network = models.CharField(max_length=64)
    removal_storage = models.BooleanField(default=False)
    price_range_min = models.CharField(max_length=64)
    price_range_max = models.CharField(max_length=64)
    dual_sim = models.BooleanField(default=False)
    charging =  models.BooleanField(default=False)
    audio_jack = models.BooleanField(default=False)


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



# newsletter
class NewsletterEmails(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    send_at = models.DateTimeField(blank=True, null=True)
    sent = models.BooleanField(default=False)

    def __str__(self):
        return self.email
