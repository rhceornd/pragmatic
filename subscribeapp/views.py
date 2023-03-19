from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})  # GET 방식으로 pk를 받겠다

    # project와 user 정보 취합
    def get(self, request, *args, **kwargs):

        # project_pk를 가진 Project를 찾고, 없다면 404
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user

        subscription = Subscription.objects.filter(user=user,
                                                   project=project)

        # toggle subscription
        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()


        return super(SubscriptionView, self).get(request, *args, **kwargs)

@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 5

    # 특정 조건에 해당하는 article을 가져올 것이기 때문에 query 수정
    def get_queryset(self):
        projects = Subscription.objects.filter(user=self.request.user).values_list('project')   # project list화
        article_list = Article.objects.filter(project__in=projects)     # field lookups
        return article_list