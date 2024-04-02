from django.urls import path
from .import views
from . import signup 


urlpatterns=[
    path('signup/',signup.signup,name='signup'),
]