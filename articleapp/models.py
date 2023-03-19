# articleapp/models.py

from django.contrib.auth.models import User
from django.db import models

from projectapp.models import Project


# Create your models here.

class Article(models.Model):
    # user가 회원탈퇴 시, 알수없음으로 나타나게
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True)

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)     # save in /media/article
    content = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
