from django.urls import path
from . import views

urlpatterns=[
    path('',views.fresh_login),
    path('shop_home',views.shop_home)
]