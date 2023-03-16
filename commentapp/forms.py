# commentapp/forms.py

from django.forms import ModelForm

from articleapp.models import Article
from commentapp.models import Comment


class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']   # writer는 서버 내에서 설정