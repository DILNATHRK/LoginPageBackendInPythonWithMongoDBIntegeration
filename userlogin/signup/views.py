from django.shortcuts import render
from django.http import JsonResponse
from .models import User


def SignUpHome(request):
    print("reached siguphome successfully")
    return JsonResponse({"status":"success","message":"reached signup home successfully"})
