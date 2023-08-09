from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sensor = models.ForeignKey(Sensor, related_name='measurements', on_delete=models.CASCADE, null=False, blank=False)
