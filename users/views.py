#-*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from users.models import User
from users.forms import LoginForm, RegisterForm
#from validate_email import validate_email


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is None:
                return render(request,
                              'users/login.html',
                              {'form': form, 'error_message': 'Пользователя с таким логином и паролем не существует'})
            else:
                login(request, user)
                return HttpResponseRedirect('../../')  # How is it better to make redirect to main page??
        else:
            print
            return render(request, 'users/login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})


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
                if User.objects.filter(email=email):
                    return HttpResponse('Почту нормально введи да!')
                else:
                    user = User(username=user_name, password=password,
                                first_name=first_name, last_name=last_name,
                                email=email)
                    user.save()
                    return HttpResponse('Пользователь зарегистрирован')

    else:
        return render(request, 'users/register.html')
