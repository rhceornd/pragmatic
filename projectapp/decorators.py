# projectapp/decorators.py

from django.http import HttpResponseForbidden
from commentapp.models import Comment
from projectapp.models import Project


# 내가 본 유저인지 보는 데코레이터
def project_ownership_required(func):
    def decorated(request, *args, **kwargs):
        comment = Project.objects.get(pk=kwargs['pk'])
        print(comment.writer, request.user)
        if not (comment.writer == request.user):
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated

