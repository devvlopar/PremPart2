from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core.mail import send_mail
import random
from  django.conf import settings
# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def fun1(request):
    return HttpResponse('ye prem ka response hai')

def create_row(request):
    Buyer.objects.create(
        first_name = 'devang',
        last_name = 'singh',
        email = 'dev@gmail.com',
        password = 'prem1234',
        address = '176, vishnunagar, udhna, surat',
        gender = 'yudasg'
    )
    return HttpResponse('row create ho gaya')

def delete_row(request):
    d_row = Buyer.objects.get(email = 'pre@gmail.com')
    d_row.delete()
    return HttpResponse('delete ho gya')

def faqs(request):
    return render(request, 'faqs.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        try:
            user_obj = Buyer.objects.get(email = request.POST['email'])
            return render(request, 'register.html',{'msg': 'Email Already Exists'})
        except:
            if request.POST['password'] == request.POST['repassword']:
                subject = "Welcome to Ecommerce"
                global user_list
                user_list = [request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password'], request.POST['repassword']]
                global computer_otp
                computer_otp = random.randint(100000, 999999) #global defined
                message = f'Your OTP is {computer_otp}.'
                from_email = settings.EMAIL_HOST_USER
                to_email = [request.POST['email']]
                send_mail(subject, message, from_email, to_email)
                return render(request, 'otp.html')
            else:
                return render(request, 'register.html',{'msg': 'Both Passwords are Not Same!!'})
            


        

def otp(request):
    if computer_otp == int(request.POST['u_otp']):
        Buyer.objects.create(
            #POST['first_name'] : ye key register.html ke form mein
            #  <input> tag mein name="first_name"
            first_name = user_list[0],
            last_name = user_list[1],
            email = user_list[2],
            password = user_list[3]
        )
        return render(request, 'register.html', {"msg":'Created Successfully'})
    else:
        return render(request, 'otp.html', {'msg': 'Invalid OTP'})