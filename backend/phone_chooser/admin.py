from django.contrib import admin
from .models import wishlist

# Register your models here.

class wishlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'link', 'image')

admin.site.register(wishlist, wishlistAdmin)