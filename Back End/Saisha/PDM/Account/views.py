from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse

def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return HttpResponse(render(request, 'signup.html', {'error':'Username has already been taken'}))
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request,user)
                return redirect("http://127.0.0.1:8000/")
        else:
            return HttpResponse(render(request, 'signup.html', {'error':'Passwords must match'}))
    else:
        # User wants to enter info
        return HttpResponse(render(request, 'signup.html'))

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect("http://www.google.com")
        else:
            return HttpResponse(render(request, 'login.html',{'error':'username or password is incorrect.'}))
    else:
        return HttpResponse(render(request, 'login.html'))

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect("http://www.google.com")