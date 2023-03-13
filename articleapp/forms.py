# articleapp/forms.py

from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'image', 'content']   # writer는 서버 내에서 설정