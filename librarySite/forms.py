from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='Имя пользователя', widget=forms.TextInput(
        attrs={"placeholder": 'Имя пользователя',
               'class': 'w-full block outline outline-1 outline-accent/70 rounded-md py-1.5 px-3'}
    ))
    password = forms.CharField(max_length=50, label='Пароль', widget=forms.PasswordInput(
        attrs={"placeholder": 'Пароль',
               'class': 'w-full block outline outline-1 outline-accent/70 rounded-md py-1.5 px-3'}
    ))


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50, label='Имя пользователя', widget=forms.TextInput(
        attrs={"placeholder": 'Имя пользователя',
               'class': 'w-full block outline outline-1 outline-accent/70 rounded-md py-1.5 px-3'}
    ))
    password1 = forms.CharField(max_length=50, label='Пароль', widget=forms.PasswordInput(
        attrs={"placeholder": 'Пароль',
               'class': 'w-full block outline outline-1 outline-accent/70 rounded-md py-1.5 px-3'}
    ))
    password2 = forms.CharField(max_length=50, label='Повторите пароль', widget=forms.PasswordInput(
        attrs={"placeholder": 'Повторите пароль',
               'class': 'w-full block outline outline-1 outline-accent/70 rounded-md py-1.5 px-3'}
    ))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
