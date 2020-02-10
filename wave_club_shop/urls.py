
from django.contrib import admin
from django.urls import path, include
from users.views import LoginView, RegisterView, SendEmailView
from goods.views import GoodsView, PriceView, GoodsListView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('buy/', GoodsView.as_view(), name='buy'),
    path('price/', PriceView.as_view(), name='price'),
    path('goodsList/', GoodsListView.as_view(), name='goodsList'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('send_email/', SendEmailView.as_view(), name='send_email'),
    path('captcha/', include('captcha.urls')),
]
