import re
from django.http import JsonResponse
from .db_connection import mongodb_connection

def home(request):
    return JsonResponse({"status":"success","message":"iam otp verification home"})

def verify_otp(request):
    if request.method!='POST':
        return JsonResponse({"status":"error","message":"invalid request method"},status=403)
    user=request.POST.dict()
    email=user.get('email')
    verification_code=user.get("verification_code")

    if not email or not verification_code:
        return JsonResponse({"status":"error","message":"email and verification code are required"},starus=400)
    result=get_otp_from_server(email,verification_code)
    if not result:
        return JsonResponse({"status": "error", "message": "User does not exist"}, status=200)
    else:
        otp=result.get("verification_code")
        if not otp:
            return JsonResponse({"status": "error", "message": "Incorrect OTP entered"}, status=200)
        elif verification_code != otp:
            return JsonResponse({"status": "error", "message": "OTP Mismatch, Retry OTP"}, status=200)
        else:
            return JsonResponse({"status": "success", "message": "OTP Verification Successful"}, status=200)

def get_otp_from_server(email, verification_code):
    client, collection, ctx = mongodb_connection()

    pattern = re.compile("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$")
    pattern_for_otp = re.compile("^[0-9]+$")

    if not pattern.match(email) or not pattern_for_otp.match(verification_code):
        return None

    user = collection.find_one({"email": email})
    if not user:
        return None

    return {"verification_code": user.get("verification_code")}