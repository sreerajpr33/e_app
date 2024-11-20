from django.urls import path
from . import views
urlpatterns=[
    path('',views.fresh_login),
    path('shop_home',views.shop_home),
    path('logout',views.freash_logout),
    path('add_product',views.addproduct),
    path('editproduct/<pid>',views.editproduct),
    path('delete_product/<pid>',views.delete_pro),
    path('register',views.register),
    path('user_name',views.user_home)
]


