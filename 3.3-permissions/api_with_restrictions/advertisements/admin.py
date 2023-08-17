from django.contrib import admin

from advertisements.models import Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'creator', 'status', 'created_at', 'updated_at')
    list_filter = ('creator', 'status')

admin.site.register(Advertisement, AdvertisementAdmin)
