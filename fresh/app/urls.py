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

    path('user_name',views.user_home),
    path('details/<pid>',views.details),
    path('addcart/<pid>',views.add_to_cart),
    path('viewcart',views.view_cart),
    path('qty_in/<cid>',views.qty_in),
    path('qty_dec/<cid>',views.qty_dec),
    path('cart_pro_buy/<cid>',views.cart_pro_buy),
    path('bookings',views.bookings),
    path('pro_buy/<pid>',views.pro_buy),
]


