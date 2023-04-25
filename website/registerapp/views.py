from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return  redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return  redirect('/registerapp/login')
    return  render(request,'login.html')

def displayreg(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['firstname']
        secondname=request.POST['secondname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exists")
                return  redirect('/registerapp/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exists")
                return  redirect('/registerapp/register')
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=secondname,email=email,password=pass1)
                user.save()
                return redirect('/registerapp/login')
        else:
            messages.info(request,"password not matched")
            return  redirect('/registerapp/register')
    return  render(request,'register.html')
def logout(request):
    auth.logout(request)
    return  redirect('/')
