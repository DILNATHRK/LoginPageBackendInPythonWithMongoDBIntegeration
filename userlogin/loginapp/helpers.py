import os
import jwt
import time
from datetime import datetime
from .db_connection import mongodb_connection

def login_secret():
    return os.getenv('LOGIN_SECRET')
def login_generate_new_token(email, password):
    secret_key = "rkd"
    expiration_time = int(time.time()) + 3600
    refresh_expiration_time = int(time.time()) + 86400

    token_payload = {
        "email": email,
        "exp": expiration_time
    }

    refresh_token_payload = {
        "exp": refresh_expiration_time
    }

    token = jwt.encode(token_payload, secret_key, algorithm="HS256")
    refresh_token = jwt.encode(refresh_token_payload, secret_key, algorithm="HS256")
    return token, refresh_token

def login_update_all_token(token,email):
    _,usercollection,ctx=mongodb_connection()
    updated_at=int(time.time())
    created_at=datetime.utcnow().isoformat()
    update_token=usercollection.update_one({"email":email},{"$set":{"token":token,"created_at":created_at}})