from django.shortcuts import render

from django.http import JsonResponse
from .models import User
import hashlib

# def login(request):
#     print("request is ",request)
#     if request.method=="POST":
#         email=request.POST.get("email")
#         password=request.POST.get("password")
#         print("input email is ",email)
#         print("input password is ",password)  
#         user=User.authenticate(email,password)
#         if user:
#             print("user is ",user)
#             return JsonResponse({"status":"success", "message":"logined successfully"})
#         else:
#             print("user is ",user)
#             return JsonResponse({"status":"failed","message":"invalid email or incorrect password"})
#     else:
#         print("user is ",user)        
#         return JsonResponse({"status":"failed","message":"request failed ,method not allowed"})

def home(request):
    print("reached home successfuully ")
    return JsonResponse({"status": "success", "message": "Hai iam from login home"})
