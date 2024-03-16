from django.urls import path
from . import views
from . import login

urlpatterns=[
    path('',views.home,name='home'),
    # path('login/',views.login,name='login'),
    path('login/',login.login,name='login'),    
]