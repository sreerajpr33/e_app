from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
import os
from django.contrib.auth.models import User



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
    if 'user' in req.session:
        return redirect(user_home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        data=authenticate(username=uname,password=password)
        if data:
            login(req,data)
            if data.is_superuser:
                req.session['shop']=uname
                return redirect(shop_home)
            else:
                req.session['user']=uname
                return redirect(user_home)
        else:
            messages.info(req, " ")
            return redirect(fresh_login)
    else:
        return render(req,'login.html')
    
def freash_logout(req):
    if 'shop' in req.session or 'user' in req.session:
        logout(req)
        req.session.flush()
        return redirect(fresh_login)
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

def editproduct(req,pid):
    if req.method=='POST':
        p_id=req.POST['pid']
        name=req.POST['name']
        dis=req.POST['dis']
        price=req.POST['price']
        off_p=req.POST['off_p']
        stock=req.POST['stock']
        file=req.FILES.get('img')
        if file:
            product.objects.filter(pk=pid).update(pid=p_id,name=name,dis=dis,price=price,offer_price=off_p,stock=stock)
            data=product.objects.get(pk=pid)
            data.img=file
            data.save()
        else:
            product.objects.filter(pk=pid).update(pid=p_id,name=name,dis=dis,price=price,offer_price=off_p,stock=stock)
        return redirect(shop_home)
    else:
        data=product.objects.get(pk=pid)
        return render(req,'shop/edit.html',{'data':data})
def delete_pro(req,pid):
    data=product.objects.get(pk=pid)
    file=data.img.url
    file=file.split('/')[-1]
    os.remove('media/'+file)
    data.delete()
    return redirect(shop_home)

# --------------------user---------------------

def register(req):
    if req.method=='POST':
        uname=req.POST['uname']
        email=req.POST['email']
        pswd=req.POST['pswd']
        try:
            data=User.objects.create_user(first_name=uname,email=email,username=email,password=pswd)
            data.save()
        except:
            messages.info(req, "already in use")
            return redirect(register)
        return redirect(fresh_login)
    else:
        return render(req,'user/register.html')

def user_home(req):
    if 'user' in req.session:
        data=product.objects.all()
        return render(req,'user/userhome.html',{'products':data})
    else:
        return redirect(fresh_login)
    
def details(req,pid):
    data=product.objects.get(pk=pid)
    return render(req,'user/details.html',{'products':data})

def add_to_cart(req,pid):
    Product=product.objects.get(pk=pid)
    user=User.objects.get(username=req.session['user'])
    try:
        Cart=cart.objects.get(Product=Product,user=user)
        Cart.qty+=1
        Cart.save()
    except:
        data=cart.objects.create(Product=Product,user=user,qty=1)
        data.save()
    return redirect(view_cart)

def view_cart(req):
    user=User.objects.get(username=req.session['user'])
    data=cart.objects.filter(user=user)
    return render(req,'user/cart.html',{'cart':data})

def qty_in(req,cid):
    data=cart.objects.get(pk=cid)
    data.qty+=1
    data.save()
    return redirect(view_cart)

def qty_dec(req,cid):
    data=cart.objects.get(pk=cid)
    data.qty-=1
    data.save()
    print(data.qty)
    if data.qty==0:
        data.delete()
    return redirect(view_cart)

def cart_pro_buy(req,cid):
    Cart=cart.objects.get(pk=cid)
    product=Cart.Product
    user=cart.user
    qty=cart.qty
    price=product.offer_price*qty
    Buy=buy.objects.create(product=product,user=user,qty=qty,price=price)
    Buy.save()
    return redirect(bookings)

def pro_buy(req,pid):
    Product=product.objects.get(pk=pid)
    user=User.objects.get(username=req.session['user'])
    qty=1
    price=Product.offer_price
    Buy=buy.objects.create(product=Product,user=user,qty=qty,price=price)
    Buy.save()
    return redirect(bookings)

def bookings(req):
    user=User.objects.get(username=req.session['user'])
    Buy=buy.objects.filter(user=user)[::-1]
    return render(req,'user/bookings.html',{'bookings':Buy})





