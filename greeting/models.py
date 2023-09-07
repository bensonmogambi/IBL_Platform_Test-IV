from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Greeting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.body