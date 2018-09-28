from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

class UserProfile(AbstractUser):
    """
        用户
    """
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name='姓名')
    bith = models.DateField(null=True, blank=True, verbose_name='出生年月')
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name='电话')
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name='邮箱')
    gender = models.CharField(max_length=6, choices=(('male', u'男'), ('female', u'女')), default='male')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

class VertifyCode(models.Model):
    """
        验证码
    """
    result = models.CharField(max_length=30, verbose_name='验证码的结果')
    img_content = models.ImageField(upload_to='captcha/', verbose_name='传入前台的图片配置')
    phone = models.CharField(max_length=11, verbose_name='电话', help_text='用户电话')

    add_time = models.DateTimeField(default=timezone.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.phone