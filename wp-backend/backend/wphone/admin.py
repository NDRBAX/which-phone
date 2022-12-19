from django.contrib import admin
from .models import *

class customUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username',  'is_active', 'is_staff', 'is_admin')

class wishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'price', 'link', 'image')

class valuesAdmin(admin.ModelAdmin):
    list_display = ('user', 'checked')

class brandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'num_devices')

class deviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand_id', 'name', 'url', 'thumbnail', 'summary')

class device_specificationsAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'spec_id', 'spec_category', 'specification', 'spec_value')

admin.site.register(Wishlist, wishlistAdmin)
admin.site.register(Values, valuesAdmin)
admin.site.register(CustomUser, customUserAdmin)
admin.site.register(Brand, brandAdmin)
admin.site.register(Device, deviceAdmin)
admin.site.register(Device_specification, device_specificationsAdmin)

