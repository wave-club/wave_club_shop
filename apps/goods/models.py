from django.db import models
from datetime import datetime 

# Create your models here.
from users.models import UserProfile

class Goods(models.Model):

    # URLField
    # class URLField([verify_exists=True, max_length=200, **options])¶
    # 保存 URL 的 CharField 。它有一个额外的可选参数：

    # URLField.verify_exists¶
    # 如果为 True (默认值)，Django 在保存对象时会检测该 URL 是否可访问(比如，网址可以正常访问，不返回404错误)。值得注意的是，如果你使用的是一个单线程开发服务器，那么验证网址会挂起当前线程。当然，对于生产用的多线程服务器来说，这就不是一个问题了。
    # Django 管理后台使用 <input type="text"> (一个单行输入框) 表示该字段。

    # 和所有 CharField 子类一样，URLField 接受可选的 max_length 参数，该参数默认值是200。

    userId = models.CharField(max_length=50)
    contact_action = models.CharField(max_length=100, verbose_name="联系方式")
    project_url = models.URLField(max_length=200, verbose_name="项目地址")
    star_num = models.IntegerField(default=0, blank=True, null=True, verbose_name="star的个数")
    follow_num = models.IntegerField(default=0, blank=True, null=True,verbose_name="follow的个数")
    fork_num = models.IntegerField(default=0, blank=True, null=True,verbose_name="fork的个数")
    watch_num = models.IntegerField(default=0, blank=True, null=True,verbose_name="watch的个数")
    start_point = models.IntegerField(default=0, blank=True, null=True,verbose_name="起始位置")
    is_flag = models.BooleanField(default=False, verbose_name="是否执行过" )
    add_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True)
    order_price = models.IntegerField(default=0, blank=True, null=True,verbose_name="订单价格")
    order_data = models.TextField(default='', blank=True, null=True,verbose_name="数据排序")
    # True 已支付
    order_payed = models.BooleanField(default=False, verbose_name="支付状态" )

    def __str__(self):
        return self.contact_action
    
    class Meta:
        verbose_name="商品信息表"
        verbose_name_plural="商品信息表"
        ordering=['star_num', 'fork_num', 'follow_num']
