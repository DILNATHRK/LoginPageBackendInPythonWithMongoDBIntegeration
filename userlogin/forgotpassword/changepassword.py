import re
from datetime import datetime
from django.http import JsonResponse
from .models import User
from .db_connection import mongodb_connection
import bcrypt

def update_password(request):
    if request.method == 'POST':
        try:
            data = request.POST.dict()
            email = data.get('email')
            password = data.get('password')
            confirm_password = data.get('confirm_password')
            if password != confirm_password:
                return JsonResponse({"status": "error", "message": "Passwords do not match"})
            if not re.match(r'^[a-zA-Z0-9.!#$%&\'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$', email):
                return JsonResponse({"status": "error", "message": "Invalid email format"})
            hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())            
            try:
                _, collection, ctx = mongodb_connection()
                update_result = collection.update_one({"email": email}, {"$set": {"password": hashed_password, "reset_password_time": datetime.utcnow()}})
                ctx.end_session()
            except Exception as e:
                return JsonResponse({"status": "error", "message": str(e)})
            
            if update_result.matched_count == 0:
                return JsonResponse({"status": "error", "message": "User does not exist"})
                
            return JsonResponse({"status": "success", "message": "Password reset successfully"})
            
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})    
    return JsonResponse({"status": "error", "message": "Invalid request method"})
