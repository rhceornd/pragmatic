# article/urls.py

from django.urls import path
from django.views.generic import TemplateView       # Template만 지정해주면 장고가 만듦


app_name = "articleapp"

# 127.0.0.1:8000/account/

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list'),
]