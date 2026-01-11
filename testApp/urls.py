from django.urls import path
from . import views

urlpatterns = [
    path("", views.timeline, name='timeline'),
    path('api/weather/', views.weather, name='weather'),
]