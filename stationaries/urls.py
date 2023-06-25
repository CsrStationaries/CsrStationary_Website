from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', views.home,name= 'home'),
    path('login',views.login,name= 'login'),
    path('signup',views.signup,name='Create Account'),
    path('logout',views.logout,name= 'logout'),
    path('logo/',views.logo),
    path('aboutus/', views.aboutus),
    path('index/', views.index),
   #path('our_product', views.our_product,"Our Products"),

]