from django.contrib import admin
from .models import Goods
# Register your models here.

"""
I am registering the models in the admin
"""

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['urserId', 'contact_action', 'add_time', 'update_time', 'order_price']
    list_filter = ['is_flag', 'order_payed']