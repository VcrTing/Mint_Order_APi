from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

from appis.business.models import Shop

User = get_user_model()
# Create your models here.

class Ratings(models.Model):
    """
        评价
    """
    RATE_TYPE = (
        (0, '满意'),
        (1, '不满意')
    )
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='用户')
    rate_time = models.DateTimeField(default=timezone.now, verbose_name='评价时间')
    rate_type = models.SmallIntegerField(choices=RATE_TYPE, verbose_name='评价类型')
    text = models.TextField(verbose_name='评价内容')

    class Meta:
        verbose_name = '评价'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text