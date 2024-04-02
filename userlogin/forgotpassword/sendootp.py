# import os
# import random
# import string
# import time
# from mailjet_rest import Client
# from datetime import datetime
# from django.http import JsonResponse
# from .db_connection import mongodb_connection
# from loginapp.helpers import login_generate_new_token,login_update_all_token

# def check_email_and_send_otp(request):
#     if request.method != 'POST':
#         return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)

#     user = request.POST.dict()
#     email = user.get("email")
    
#     if not email:
#         return JsonResponse({"status": "error", "message": "Email is required"}, status=400)

#     counts = fetching_user_details_by_email(email)
#     if counts > 0:
#         token, err = send_otp_email(email)
#         if err:
#             return JsonResponse({"status": "error", "message": "Failed to send OTP email"}, status=200)
#         else:
#             return JsonResponse({"status": "success", "message": "OTP Sent Successfully", "token": token}, status=200)
#     else:
#         return JsonResponse({"status": "error", "message": "Email Doesn't Exist"}, status=503)

# def fetching_user_details_by_email(email):
#     client, _, _ = mongodb_connection()
#     collection = client.userlogin.userdetails
#     res = collection.count_documents({"email": email})
#     return res

# def generate_random_otp():
#     # Generate a random 6-digit OTP
#     otp = ''.join(random.choices(string.digits, k=6))
#     return otp

# def send_otp_email(email):
#     try:
#         print("email is ", email)
#         _, collection, ctx = mongodb_connection()
#         otp_str = generate_random_otp()
#         otp = int(otp_str)
#         print("generated otp ", otp)
#         token, _ = login_generate_new_token(email, otp_str)
#         login_update_all_token(token, email)
#         print("generated token is ", token)
#         reset_password_time = datetime.utcnow().isoformat()

#         filter = {"email": email}
#         update = {"$set": {"verification_code": otp_str, "reset_password_time": reset_password_time}}
#         print("update set is ", update)
#         print("collection is ", collection)
#         mailjet_client = Client(auth=('82e5834f4da9f991c64d62c9f4a233a7', '2f31978bfeff017f99c23683b5cfe7ef'), version='v4')
#         if not mailjet_client:
#             return None, "Failed to create Mailjet client"        
#         print("Mailjet client created",mailjet_client) 

#         result = collection.update_one(filter, update)
#         if result is None:
#             # Document to update was not found
#             print("No document found to update")
#             return None, "No document found to update"
        
#         print("update result is ", result)
#         print("Matched document count:", result.matched_count)
#         print("Modified document count:", result.modified_count)
        
#         # mailjet_client,err = mailjet.Client(auth=("881af34c8dc64935d5e0d1d9da450db9", "985a0b3093d0eb532c8005e4660b5b8d"), version='v4')
#         message = {
#             'From': {'Email': 'rkdilnath@gmail.com', 'Name': 'rkd'},
#             'To': [{'Email': email}],
#             'Subject': 'Your One Time OTP',
#             'TextPart': f'Your OTP is: {otp}',
#             'HTMLPart': f'<h3>Your OTP is: {otp}</h3>'
#         }
#         print("Sending email to:", email)
#         print("Email content:", message)        
#         result, err = mailjet_client.send.create(data=message)
#         print("Mailjet API response:", result)
#         print("Mailjet API error:", err)
#         if result.status_code == 200:
#             return token, None
#         else:
#             return None, "Failed to send OTP email"
#     except Exception as e:
#         return None, e



import os
import random
import string
import time
from datetime import datetime
from django.http import JsonResponse
from django.core.mail import send_mail
from .db_connection import mongodb_connection
from loginapp.helpers import login_generate_new_token, login_update_all_token

def check_email_and_send_otp(request):
    if request.method != 'POST':
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)

    user = request.POST.dict()
    email = user.get("email")
    
    if not email:
        return JsonResponse({"status": "error", "message": "Email is required"}, status=400)

    counts = fetching_user_details_by_email(email)
    if counts > 0:
        token, err = send_otp_email(email)
        if err:
            return JsonResponse({"status": "error", "message": "Failed to send OTP email"}, status=200)
        else:
            return JsonResponse({"status": "success", "message": "OTP Sent Successfully", "token": token}, status=200)
    else:
        return JsonResponse({"status": "error", "message": "Email Doesn't Exist"}, status=503)

def fetching_user_details_by_email(email):
    client, _, _ = mongodb_connection()
    collection = client.userlogin.userdetails
    res = collection.count_documents({"email": email})
    return res

def generate_random_otp():
    # Generate a random 6-digit OTP
    otp = ''.join(random.choices(string.digits, k=6))
    return otp

def send_otp_email(email):
    try:
        print("email is ", email)
        _, collection, ctx = mongodb_connection()
        otp_str = generate_random_otp()
        otp = int(otp_str)
        print("generated otp ", otp)
        token, _ = login_generate_new_token(email, otp_str)
        login_update_all_token(token, email)
        print("generated token is ", token)
        reset_password_time = datetime.utcnow().isoformat()

        filter = {"email": email}
        update = {"$set": {"verification_code": otp_str, "reset_password_time": reset_password_time}}
        print("update set is ", update)
        print("collection is ", collection)
        
        result = collection.update_one(filter, update)
        if result is None:
            # Document to update was not found
            print("No document found to update")
            return None, "No document found to update"
        
        print("update result is ", result)
        print("Matched document count:", result.matched_count)
        print("Modified document count:", result.modified_count)
        
        # Send email using Django's send_mail function
        subject = 'Your One Time OTP'
        message = f'Your OTP is: {otp}'
        sender_email = 'rkdilnath@gmail.com'  # Update with your sender email address
        recipient_list = [email]
        
        send_mail(subject, message, sender_email, recipient_list)
        
        return token, None
    except Exception as e:
        return None, e
