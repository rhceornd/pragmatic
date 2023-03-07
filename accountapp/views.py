from django.shortcuts import render, redirect

# Create your views here.
# accountapp/views.py

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from accountapp.models import HelloWorld


# Create your views here.

def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('hello_world_input')    # html에서 받은 hello_world_input을 받음

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()         # DB에 저장

        # return HttpResponseRedirect(reverse('accountapp:hello_world'))
        return redirect('accountapp:hello_world')
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})


