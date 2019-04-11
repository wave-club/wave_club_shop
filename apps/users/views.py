# _*_ encoding: utf-8 _*_
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, hashers
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse

from .models import UserProfile
from .forms import LoginForm, RegisterForm

from utils.email_send import send_register_email
from apiData.result import Result


# Create your views here.


class SendEmailView(View):

    def post(self, request):
        send_email = request.POST.get('email', '')
        print(send_email)
        if send_email:
            send_register_email(send_email, "register")
            return HttpResponse('发送成功')
        else:
            return HttpResponse('发送失败')      

class RegisterView(View):
    
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {
            'register_form': register_form
        }) 
    
    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('username', '')
            password = request.POST.get('password', '')
            name = request.POST.get('name', '')
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.name = name
            user_profile.password = make_password(password)
            user_profile.save()

            # send_register_email(user_name, "register")
            return redirect('/login/')
        else:
            return render(request, 'register.html', {'register_form': register_form})    

class LoginView(View):
    
    def get(self, request):
        userid = request.session.get('_auth_user_id')

        if userid is not None:
            return redirect('/buy/') 
        return render(request, 'login.html', {}) 


    def post(self, request):

        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(request, username=user_name, password=password)
            if user is not None:
                login(request, user)
                return redirect('/buy/')
            else:
                return render(request, 'login.html', {'msg': '账号密码不对', 'login_form': login_form})    
        else:
            return render(request, 'login.html', {'msg': '账号密码不对', 'login_form': login_form})
