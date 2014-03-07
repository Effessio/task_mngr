#-*- coding:utf-8 -*_
from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from users.models import User
from validate_email import validate_email


def user_login(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']
        user = authenticate(username=user_name, password=password)
        if user is None:
            return HttpResponse('bad')
        else:
            login(request, user)
            return HttpResponse('good')
    else:
        return render(request, 'users/login.html')


def user_register(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['e-mail']
        if password != password2 or len(password) == 0:
            return HttpResponse('Пароль введи нормально да!')
        else:
            if User.objects.filter(username=user_name):
                return HttpResponse('Такой пользователь уже существует')
            else:
                if not validate_email(email) or User.objects.filter(email=email):
                    return HttpResponse('Почту нормально введи да!')
                else:
                    user = User(username=user_name, password=password,
                                first_name=first_name, last_name=last_name,
                                email=email)
                    user.save()
                    return HttpResponse('Пользователь зарегистрирован')

    else:
        return render(request, 'users/register.html')
