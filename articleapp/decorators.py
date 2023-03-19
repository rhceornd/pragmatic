# articleapp/decorator.py

from django.http import HttpResponseForbidden
from articleapp.models import Article


# 내가 본 유저인지 보는 데코레이터
def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk'])
        print(article.writer, request.user)
        if not (article.writer == request.user):
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated
