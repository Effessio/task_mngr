# -*- coding: utf-8 -*-
from django import forms
from users.models import User


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
                                                                                'class': 'form-control',
                                                                                'placeholder': 'Password'}))

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if (not password) and (not username):
            raise forms.ValidationError(u'Вы вообще ничего не ввели')
        if not password:
            raise forms.ValidationError(u'Вы не ввели пароль')
        if not username:
            raise forms.ValidationError(u'Вы не ввели имя пользователя')
        return cleaned_data



class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Password again'}))

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        username = cleaned_data.get('username')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if User.objects.filter(username=username):
            raise forms.ValidationError(u'Пользователь с таким именем уже существует')
        if User.objects.filter(email=email):
            raise forms.ValidationError(u'Пользователь с таким адресом электронной почты уже существует')
        if password != confirm_password:
            raise forms.ValidationError(u'Введенные пароли не совпадают')
        if len(password) < 5:
            raise forms.ValidationError(u'Пароль слишком маленький. Увеличте до 5 символов')
        return cleaned_data