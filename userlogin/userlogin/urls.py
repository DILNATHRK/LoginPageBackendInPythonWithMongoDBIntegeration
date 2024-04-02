
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loginapp.urls')), 
    path('',include('signup.urls')),
    path('',include('forgotpassword.urls')),
]
