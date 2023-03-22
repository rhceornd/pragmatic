# accountapp/views.py
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from articleapp.models import Article

has_ownership = [account_ownership_required, login_required]

@login_required # if login, do func. Or go to login
def hello_world(request):

    if request.method == "POST":

        temp = request.POST.get('hello_world_input')    # html에서 받은 hello_world_input을 받음

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()         # DB에 저장

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
        # return redirect('accountapp:hello_world')
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})



# Create view
class AccountCreateView(CreateView):    # class based view. 장고에서 user 관련하여 지원해줌
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world') # 어느 경로로 다시 재배정    class는 reverse_lazy 사용
    template_name = 'accountapp/create.html'

# Read view
class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    paginate_by = 25

    # 어떠한 게시글을 가지고 올 것인지 작성. get_context_data는 장고에서 제공해줌, --> template에서 object_list 사용
    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())  # writer의 모든 object를 가져옴
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)

# Update view
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'


# Delete view
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

# method_decorator는 def에서 사용하는 decorator를 class에서도 사용할 수 있도록 해줌
'''
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
@method_decorator(account_ownership_required, 'get')
@method_decorator(account_ownership_required, 'post')

==
has_ownership = [account_ownership_required, login_required]
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
'''

