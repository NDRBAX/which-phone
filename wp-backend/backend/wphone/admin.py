from django.contrib import admin
from .models import wishlist, values

# Register your models here.
class wishlistAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'link', 'image')

class valuesAdmin(admin.ModelAdmin):
    list_display = ('step', 'label', 'checked')
admin.site.register(wishlist, wishlistAdmin)
admin.site.register(values, valuesAdmin)