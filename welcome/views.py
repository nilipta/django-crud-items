from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth, messages
from django.contrib.auth.models import User

# Create your views here.


def loginForm (request):
    print('login process started')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email)
        print(password)

        if email == "" or password == "":
            messages.error(request,'Fill the valid data in credentials')
            return redirect('/auth') 
        if User.objects.filter(email=email).exists():
            userName = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=userName, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login realizado com sucesso, Bem Vindo {} !'.format(user))
                print('user is good')
                return redirect ('/owner')
            else:
                print('user is NOT good')

    return redirect('/auth')


def authPage (request):
    return render(request, 'welcome/login.html')

def signup(request):
    print('now new user will sign up')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email)
        print(password)

        if email == "" or password == "":
            messages.error(request,'Fill the valid data in credentials')
            return redirect('/auth') 
        else:
            return redirect ('/owner')

    return redirect('/auth')