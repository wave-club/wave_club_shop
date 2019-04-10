"""wave_club_shop URL Configuration

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
from django.urls import path, include
from django.views.generic import TemplateView
from users.views import LoginView, RegisterView
from goods.views import GoodsView, PriceView, GoodsListView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('buy/', GoodsView.as_view(), name='buy'),
    path('price/', PriceView.as_view(), name='price'),
    path('goodsList/', GoodsListView.as_view(), name='goodsList'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('captcha/', include('captcha.urls')),
]
