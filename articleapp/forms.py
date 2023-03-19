# articleapp/forms.py
from django import forms
from django.forms import ModelForm

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    # to customize (WYSIWYG). editable과 style class를 만들고(css) model에 있는 content에 넣어 article create.html에 넣어줌
    # TODO text-left 적용 안됨. 나중에 체크. style도 굳이 안넣어도 됨
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-left',   # text-left가 안먹
                                                           'style': 'height: auto;'}))
    # project 선택을 안해도 article 작성 가능하게
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)

    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']   # writer는 서버 내에서 설정