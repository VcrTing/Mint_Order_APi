from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

from appis.business.models import Shop
from appis.operation.models import Ratings

User = get_user_model()
# Create your models here.

class Recommend(models.Model):
    """
        推荐
    """
    name = models.CharField(max_length=120, verbose_name='推荐名称')

    class Meta:
        verbose_name = '食品的推荐'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class FoodImages(models.Model):
    """
        菜的宣传图片
    """
    image = models.ImageField(upload_to='goods/foods/images', verbose_name='菜的宣传图片')

    class Meta:
        verbose_name = '菜的宣传图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.image

class Foods(models.Model):
    """
        菜
    """
    name = models.CharField(max_length=120, verbose_name='名称')
    price = models.FloatField(verbose_name='价格')
    old_price = models.FloatField(verbose_name='原价')
    description = models.CharField(max_length=200, verbose_name='描述')
    sell_count = models.IntegerField(verbose_name='总售量')
    rating = models.IntegerField(verbose_name='总评价量')
    info = models.CharField(verbose_name='信息')
    icon = models.ImageField(upload_to='goods/foods/icon', verbose_name='图标')
    image = models.ImageField(upload_to='goods/foods/image', verbose_name='图片')

    foods = models.ManyToManyField(Ratings,  verbose_name='所属菜')
    images = models.ManyToManyField(FoodImages, verbose_name='所属宣传图')

    class Meta:
        verbose_name = '菜'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Goods(models.Model):
    """
        可卖商品
    """
    name = models.CharField(max_length=60, verbose_name='商家的食品分类的名称')
    icon = models.ImageField(upload_to='goods/icon', verbose_name='图标')

    foods = models.ManyToManyField(Foods, verbose_name='食物')

    class Meta:
        verbose_name = '食品大揽'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
