from django.contrib import admin
from .models import *


class customUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username','avatar_url', 'is_active', 'is_staff', 'is_admin', 'wishlist_len', 'history_len')

    def wishlist_len(self, obj):
        return obj.wishlist.count()
    wishlist_len.short_description = 'Wishlist length'

    def history_len(self, obj):
        return obj.history.count()
    history_len.short_description = 'Number of searches'



class brandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'num_devices')


class deviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand_id', 'name', 'url', 'thumbnail', 'summary')


class device_specificationsAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'spec_id', 'spec_category',
                    'specification', 'spec_value')

class newsletterEmailsAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')

admin.site.register(CustomUser, customUserAdmin)
admin.site.register(Brand, brandAdmin)
admin.site.register(Device, deviceAdmin)
admin.site.register(Device_specification, device_specificationsAdmin)
admin.site.register(NewsletterEmails, newsletterEmailsAdmin)


