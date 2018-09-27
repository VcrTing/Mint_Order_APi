from django.db import models

# Create your models here.

class Location(models.Model):

    address = models.CharField(max_length=200, verbose_name='地址')
    name = models.CharField(max_length=200, verbose_name='显示地址')
    geohash = models.CharField(max_length=120, verbose_name='经度,纬度')
    latitude = models.FloatField(verbose_name='经度')
    longitude = models.FloatField(verbose_name='纬度')

    class Meta:
        verbose_name = '获取位置的接口'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name