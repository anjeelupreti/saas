from django.shortcuts import render,redirect
from django.contrib.auth import authenticate ,logout
from django.http import HttpResponseBadRequest
from django.contrib.auth import get_user_model

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate ,login , logout
from django.contrib import messages
# User=get_user_model()



def account_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully !")
    return redirect('/home/')


# def login_view(request):
#     if request.method == "POST":
#         username = request.POST["username"] or None # Use `.get()` to avoid errors
#         password = request.POST["password"] or None

#         if not username or not password:
            
#             return HttpResponseBadRequest("Username and password are required.")

#         # Authenticate user
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             return redirect("home")
#         else:
#             return render(request, "user/login.html", {"error": "Invalid credentials"})

#     return render(request, "user/login.html")

# def register_view(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         email=request.POST['email']
#         password=request.POST['password']
#         username_exists=User.objects.filter(username__iexact=username).exists()
#         email_exists=User.objects.filter(email__iexact=email).exists()
#         if not username_exists and email_exists:
#             User.objects.create_user(username, email=email,password=password)
#         else:
#             error_message='User with similar information exists'
#     context={
#         error_message:error_message
        
#     }
#     return render (request,'user/register.html',context)