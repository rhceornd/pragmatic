from django.urls import path, include

app_name = 'profileapp'

urlpatterns = [
    path('accounts/', include('accountapp.urls')),
    path('profiles/', include('profileapp.urls')),
]
