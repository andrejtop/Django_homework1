from django.contrib import admin

from .models import *

class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('id', 'temperature', 'created_at')

class SensorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

admin.site.register(Measurement, MeasurementAdmin)
admin.site.register(Sensor, SensorAdmin)

