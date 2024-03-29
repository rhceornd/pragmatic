from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


# Create your views here.

class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/create.html'


    '''
    profileapp의 model에 있는 User 내용은 form에는 없는 이유 :
    user 정보가 form에 쓰이면 타인에게 노출되기 때문에 서버내에서 처리해야함
    ==================================================================
    def form_valid(self, form):
        return super().form_valid(form)
    --> 이렇게 작성하면 기존 form의 내용이 form_valid의 form 인자에 그대로 들어감
    '''
    def form_valid(self, form):
        temp_profile = form.save(commit=False)      # 서버로 보내진 않음
        temp_profile.user = self.request.user       # user 데이터를 당사자 user로 적용
        temp_profile.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})     # object는 ProfileCreateView의 Profile을 가르킴

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})