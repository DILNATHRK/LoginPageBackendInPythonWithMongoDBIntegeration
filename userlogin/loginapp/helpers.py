import os
import jwt
import time
from .db_connection import mongodb_connection

def login_secret():
    return os.getenv('LOGIN_SECRET')
def login_generate_new_token(email,password,role):
    secret_key="rkd"
    expiration_time=int(time.time())+3600
    refresh_expiration_time=int(time.time())+86400

    token.payload={
        "email":email,
        "role":role,
        "exp":expiration_time
    }

    refresh_token.payload={
        "exp":refresh_expiration_time
    }

    token=jwt.encode(token.payload,secret_key,algorithm="HS256")
    refresh_token=jwt.encode(refresh_token.payload,secret_key,algorithm="HS256")
    return token,refresh_token

def login_update_all_token(token,email,role):
    _,usercollection,ctx=mongodb_connection()
    updated_at=int(time.time())
    update_token=usercollection.update_one({"email":email},{"set":{"token":token,"updated_at":updated_at}})