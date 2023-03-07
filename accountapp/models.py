from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)

