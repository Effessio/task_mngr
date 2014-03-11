# -*- coding: utf-8 -*-
from django import forms


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
    username = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()
