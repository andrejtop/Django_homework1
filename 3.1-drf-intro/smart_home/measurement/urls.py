from django.urls import path
from .views import *

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensor/<int:pk>/', SensorView.as_view()),
    path('sensors/<int:pk>/', SingleSensorView.as_view()),
    path('measurements/', MeasurementView.as_view()),
]
