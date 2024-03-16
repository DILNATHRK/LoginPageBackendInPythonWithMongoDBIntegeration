from datetime import timedelta,datetime
import bcrypt
import os
import jwt
from . import helpers
from .db_connection import mongodb_connection
from django.http import JsonResponse

# def verify_password(user_password,provided_password):
#     try:
#         bcrypt.checkpw(provided_password.encode(),user_password.encode())
#         return True,None
#     except bcrypt.hashpw(user_password.encode(),bcrypt.gensalt()):
#         return False,"Incorrect password"

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password

def verify_password(provided_password, hashed_password):
    try:
        # Encode hashed password as bytes
        hashed_password_bytes = hashed_password.encode('utf-8')
        
        if bcrypt.checkpw(provided_password.encode(), hashed_password_bytes):
            return True, "Password matched!"
        else:
            return False, "Password mismatch!"
    except ValueError:
        return False, "Invalid salt"
    except Exception as e:
        return False, f"Error: {e}"



def login(request):
    _,collection,ctx=mongodb_connection()
    data=request.POST
    email=data.get('email')
    password=data.get('password')

    found_user=collection.find_one({"email":email})
    if not found_user:
        return JsonResponse({"status":"error","message":"email or password is incorrect"})
    password_is_valid,message=verify_password(found_user['password'],password)
    if not password_is_valid:
        return JsonResponse({"status":"error","message":message},status=400)
    if found_user['status']!=1:
        return JsonResponse({"status":"error","message":"access not available on this account !contact admin"})
    
    token,refresh_token=helpers.login_generate_new_token(found_user['email'],found_user['password'],found_user['role'])
    helpers.login_update_all_token(token,found_user['email'],found_user['role']) 

    return JsonResponse({"status":"success","message":"logined successfully","token":token,"refresh_token":refresh_token})   
