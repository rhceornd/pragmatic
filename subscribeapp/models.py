from django.contrib.auth.models import User
from django.db import models

from projectapp.models import Project


# Create your models here.

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='subscription')

    # user와 project 쌍이 가지는 구독은 하나만
    class Meta:
        unique_together = ('user', 'project')