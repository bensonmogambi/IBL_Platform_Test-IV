from django.urls import path
from .views import greeting

urlpatterns = [
    path('greeting/', greeting, name='greeting-api'),
]