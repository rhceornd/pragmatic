# profileapp/decorater.py

from django.http import HttpResponseForbidden

from profileapp.models import Profile


# url의 update에서 받는 pk로 받아 profile 주인 확인
def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):

        profile = Profile.objects.get(pk=kwargs['pk'])

        if not (profile.user == request.user):
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated

