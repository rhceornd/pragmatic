'''
app.
1. python manage.py startapp comment
2. add comment in setting
3. urls.py
4. make views.py and define model
5.model.py modeling what you define in views.py
6. forms.py
7. makemigrations
'''

# commentapp/urls.py

from django.urls import path

from commentapp.views import CommentCreateView, CommentDeleteView

app_name = "commentapp"

# 127.0.0.1:8000/article/

urlpatterns = [
    path('create/', CommentCreateView.as_view(), name='create'),
    path('delete/<int:pk>', CommentDeleteView.as_view(), name='delete'),

]