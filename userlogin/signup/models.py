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
        db_table = 'loginapp_userdetails'

    @staticmethod
    def authenticate(email, password):
        print("input email is:", email)
        print("input password is:", password)
        try:
            # Access MongoDB collection
            collection = mongodb_connection.db.userdetails
            print("Collection:", collection)
            # Retrieve user from MongoDB
            user = collection.find_one({"email": email})
            print("Retrieved user:", user)
            if user:
                hashed_password = hashlib.md5(password.encode()).hexdigest()
                print("Hashed password:", hashed_password)
                print("User password:", user['password'])
                if user['password'] == hashed_password:
                    print("Password matched!")
                    return user
                else:
                    print("Password mismatch!")
                    return None
            else:
                print("User does not exist!")
                return None
        except Exception as e:
            print("Error:", e)
            return None
