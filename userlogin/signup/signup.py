from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .helper import signup_user


@csrf_exempt
def signup(request):
    if request.method=='POST':
        name=request.POST.get("name")
        email=request.POST.get('email')
        password=request.POST.get('password')
        number=request.POST.get('number')
        print("name is ",name)
        print("email is ",email)
        print("password is ",password)
        print("number is ",number)

        if not name or not email or not password or not number:
            return JsonResponse({'status':"success","message":"all fields are required"},status=400)
        result,message=signup_user(name,email,password,number)
        if result:
            return JsonResponse({"status":"success","message":message})
        else:
            return JsonResponse({"status":"error","message":message},status=500)
    else:
        return JsonResponse({'status':"error","message":"method not allowed"},status=405)
        