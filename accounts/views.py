from django.http import HttpResponse
from django.shortcuts import redirect,render
import uuid
from .models import Profile
from django.conf import settings
from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
# Create your views here.

def login_user(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(username = email)
        
        if not user.exists():
            messages.warning(request,'Account not found')
            return redirect(request.path_info)
        
        if not user[0].profile.is_email_verified:
            messages.warning(request,'Your email is not verified')
            return redirect(request.path_info)
        
        user= authenticate(username=email,password=password)
        if user:
            login(request,user)
            return redirect('/')
        
        messages.warning(request,'Invalid Credentials')
        return redirect(request.path_info)
    return render(request,'login.html')
            
def logout(request):
    logout(request)
    messages.success(request,'You have successfully logged out.')
    return redirect(request,'login.html')


def signup(request):
    if request.method=='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(username = email)
        
        if user.exists():
            messages.warning(request, 'Email is already taken.')
            return redirect(request.path_info)
        user=User.objects.create(first_name=first_name,last_name=last_name,email=email,username=email)
        user.set_password(password)
        user.save()
        messages.success(request, 'An email has been sent to ur email.')

        return render(request,'login.html')
    return render(request,'signup.html')
        

        
def send_activation_email(email,email_token):
    subject='Your account needs to be verified'
    email_from=settings.EMAIL_HOST_USER
    message=f'Hi, click on the link to activate your account http://127.0.0.1:8000/accounts/activate/{email_token}'
    send_mail(subject,message,email_from,[email])
    
@receiver(post_save,sender=User)
def send_email_token(sender,instance,created,**kwargs):
    try:
        if created:
            email_token=str(uuid.uuid4())
            Profile.objects.create(user=instance,email_token=email_token)
            email=instance.email
            send_activation_email(email,email_token)
            print(f"Activation email sent to {email}")
    except Exception as e:
        print(str(e))
        
def activate_email(request,email_token):
    try:
        user=Profile.objects.get(email_token=email_token)
        user.is_email_verified=True
        user.save()
        return redirect('/')
    except Exception as e:
        print(str(e))