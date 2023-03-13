# profileapp/models.py

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

'''
Profile model을 사용하기 위해서는 views.py에서 보듯 form이 필요
대체적으로 model과 form 형태가 유사하여 django에서 ModelForm이라는 함수를 제공
이를 통하여 Profile을 상속받아 form을 쉽게 만들 수 있음.
profileapp.forms.ProfileCreationForm
'''
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')   # Profile and user 1:1 matching

    image = models.ImageField(upload_to='profile/', null=True)  # /media/profile 에 저장
    nickname = models.CharField(max_length=20, unique=True, null=True)  # class Profile 안에서 unique 해야함
    message = models.CharField(max_length=100, null=True)