from django.shortcuts import render

# Create your views here.
# accountapp/views.py

from django.http import HttpResponse
from django.shortcuts import render

from accountapp.models import HelloWorld


# Create your views here.

def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('hello_world_input')    # html에서 받은 hello_world_input을 받음

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()         # DB에 저장


        return render(request, 'accountapp/hello_world.html', context={'hello_world_output': new_hello_world})
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD!!!'})


