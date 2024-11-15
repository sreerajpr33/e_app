from django.urls import path
from . import views
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.fresh_login),
    path('shop_home',views.shop_home),
    path('logout',views.freash_logout),
    path('add_product',views.addproduct),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
