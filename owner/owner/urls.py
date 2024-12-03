"""owner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from customer import views

from django.conf.urls import url
from django.contrib import admin
from django.urls import path
urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$',views.insertindex,name='insertindex'),
    url('insertindex', views.insertindex, name='insertindex'),

    url('insertlogin',views.insertlogin,name='insertlogin'),
    url("logcheck", views.logcheck, name="logcheck"),
    url("changepassword", views.changepassword, name="changepassword"),

    url('insertCustRegistration',views.insertCustRegistration,name='insertCustRegistration'),
    url('insertfeedback', views.insertfeedback, name='insertfeedback'),
    url('insertAddProduct', views.insertAddProduct, name='insertAddProduct'),
    url('insertOrderRequest', views.insertOrderRequest, name='insertOrderRequest'),
    url('insertPaymentInfo', views.insertPaymentInfo, name='insertPaymentInfo'),

    url('showproduct',views.showproduct, name='showproduct'),
    url('productreg_del/(?P<pk>\d+)/$', views.productreg_del, name='productreg_del'),

    url('showCustRegistration', views.showCustRegistration, name='showCustRegistration'),
    url('custreg_del/(?P<pk>\d+)/$', views.custreg_del, name='custreg_del'),

    url('showShopReg', views.showShopReg, name='showShopReg'),
    url('shopcustreg_del/(?P<pk>\d+)/$', views.shopcustreg_del, name='shopcustreg_del'),

    url('showFeedback', views.showFeedback, name='showFeedback'),
    url('Feedbackreg_del/(?P<pk>\d+)/$', views.Feedbackreg_del, name='Feedbackreg_del'),

    url('showOrderRequest', views.showOrderRequest, name='showOrderRequest'),
    url('OrderRequestreg_del/(?P<pk>\d+)/$', views.OrderRequestreg_del, name='OrderRequestreg_del'),

    url('showPaymentInfo', views.showPaymentInfo, name='showPaymentInfo'),

    url('sendpass', views.sendpass, name='sendpass'),
    url('logout', views.logout, name='logout'),

]


