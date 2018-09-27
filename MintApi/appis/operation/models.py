from django.db import models
from django.contrib.auth import get_user_model

from appis.business.models import Shop

User = get_user_model()
# Create your models here.

class Ratings(models.Model):
    """
        评分
    """
    rating = models.FloatField(verbose_name='单个评分')
    shop = models.ForeignKey(to=Shop, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='商家')
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='用户')

    class Meta:
        verbose_name = '评分'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.rating