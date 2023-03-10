# accountapp/views.py

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld

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
class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'