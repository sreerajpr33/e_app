from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages



# Create your views here.

def shop_home(req):
    return render(req,'shop/home.html')

def fresh_login(req):
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        data=authenticate(username=uname,password=password)
        if data:
            login(req,data)
            return redirect(shop_home)
        else:
            return redirect(fresh_login)
    else:
        return render(req,'login.html')
    