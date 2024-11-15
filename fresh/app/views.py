from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *



# Create your views here.

def shop_home(req):
    if 'shop' in req.session:
        data=product.objects.all()
        return render(req,'shop/home.html',{'products':data})
    else:
        return redirect(fresh_login)

def fresh_login(req):
    if 'shop' in req.session:
        return redirect(shop_home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        data=authenticate(username=uname,password=password)
        if data:
            login(req,data)
            req.session['shop']=uname
            return redirect(shop_home)
        else:
            messages.info(req, "")
            return redirect(fresh_login)
    else:
        return render(req,'login.html')
    
def freash_logout(req):
    if 'shop' in req.session:
        return render(req,'shop/home.html')
    else:
        return redirect(fresh_login)
    
def addproduct(req):
    if 'shop' in req.session:
        if req.method=='POST':
            pid=req.POST['pid']
            name=req.POST['name']
            dis=req.POST['dis']
            price=req.POST['price']
            off=req.POST['off_price']
            stock=req.POST['stock']
            file=req.FILES['img']   
            data=product.objects.create(pid=pid,name=name,dis=dis,price=price,offer_price=off,stock=stock,img=file)
            data.save()
            return redirect(shop_home)
        else:
            return render(req,'shop/product.html')
    else:
        return redirect(fresh_login)