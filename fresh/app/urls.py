from django.urls import path
from . import views
from django.urls import path,include



urlpatterns=[
    path('',views.fresh_login),
    path('shop_home',views.shop_home),
    path('logout',views.freash_logout),
    path('add_product',views.addproduct),
    path('editproduct/<pid>',views.editproduct),
]


