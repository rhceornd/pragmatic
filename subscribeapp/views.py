from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from projectapp.models import Project
from subscribeapp.models import Subscription


# Create your views here.

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