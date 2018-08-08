"""route_distribute URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,re_path
# from django.conf.urls import include
# 2.0 以后匹配正则要使用 re_path
from app01 import views
urlpatterns = [
    path('login/', views.login),
    path('index/', views.index),
    path('orm/', views.orm),
    path('user_info/', views.user_info),
    path('user_group/', views.user_group),
    re_path('user_detail-(?P<nid>\d+)/', views.user_detail)

]
