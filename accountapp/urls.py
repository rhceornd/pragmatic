# accountapp/urls.py

from django.contrib import admin
from django.urls import path
# from . import views

from accountapp.views import hello_world, AccountCreateView

app_name = "accountapp"

# 127.0.0.1:8000/account/

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),                  # 함수형 뷰는 이름을 넣음
    path('create/', AccountCreateView.as_view(), name='create'), # 클래스형 뷰는 as_view() 추가
]
