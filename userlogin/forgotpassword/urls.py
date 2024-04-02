from django.urls import path
from . import views
from . import sendootp
from . import otpverification
from . import changepassword

urlpatterns=[
    path('sendotp/',sendootp.check_email_and_send_otp),
    path('verifyotp/',otpverification.verify_otp),
    path('changepassword/',changepassword.update_password)
]