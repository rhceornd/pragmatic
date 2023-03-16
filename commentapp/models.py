# commentapp/models.py
from django.contrib.auth.models import User
from django.db import models

from articleapp.models import Article


# Create your models here.

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, related_name='comment')  # server 단에서 확인 : create,html에 hidden input 넣음
    write = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment')       # server 단에서 확인

    content = models.TextField(null=False)      # 입력 받음
    created_at = models.DateTimeField(auto_now=True)    # 자동생성