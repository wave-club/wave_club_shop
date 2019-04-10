from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    name = models.CharField(max_length=30, blank=True, null=True, verbose_name="姓名")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="用户信息"
        verbose_name_plural="用户信息"
