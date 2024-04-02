from django.db import models
import logging
import hashlib
from datetime import datetime
from .db_connection import mongodb_connection

logger = logging.getLogger(__name__)

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)
    loginpassword = models.CharField(max_length=100)
    confirmpassword = models.CharField(max_length=100)
    number = models.CharField(max_length=12)
    verificationcode = models.CharField(max_length=6, blank=True, null=True, default=None)
    reset_password_time = models.DateTimeField(blank=True, null=True, default=None)
    token = models.CharField(max_length=100, blank=True, null=True, default=None)
    refresh_token = models.CharField(max_length=100, blank=True, null=True, default=None)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=100)
    status = models.IntegerField(default=0)

    class Meta:
        db_table = 'forgotpasswordapp_userdetails'

 