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

    add_time = models.DateTimeField(default=timezone.now, verbose_name='添加时间', help_text='添加时间')

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

    add_time = models.DateTimeField(default=timezone.now, verbose_name='添加时间', help_text='添加时间')

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
    info = models.CharField(max_length=120, verbose_name='信息')
    icon = models.ImageField(upload_to='goods/foods/icon', verbose_name='图标')
    image = models.ImageField(upload_to='goods/foods/image', verbose_name='图片')

    foods = models.ManyToManyField(Ratings,  verbose_name='所属菜')
    images = models.ManyToManyField(FoodImages, verbose_name='所属宣传图')

    add_time = models.DateTimeField(default=timezone.now, verbose_name='添加时间', help_text='添加时间')

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

    add_time = models.DateTimeField(default=timezone.now, verbose_name='添加时间', help_text='添加时间')

    class Meta:
        verbose_name = '食品大揽'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Discounts(models.Model):
    """
        减免优惠活动
    """
    DIS_TYPE = (
        (0, '首单'),
        (1, '满减'),
        (2, '特价')
    )
    name = models.CharField(max_length=12, verbose_name='名称')
    content = models.CharField(max_length=120, verbose_name='减免内容')
    type = models.SmallIntegerField(choices=DIS_TYPE, verbose_name='减免类型')

    old_price = models.FloatField(verbose_name='原价/满价为多少')
    offset_price = models.FloatField(verbose_name='立减/其他的价格')

    is_overlay = models.BooleanField(verbose_name='该优惠是否可叠加')
    is_only_for_food = models.BooleanField(verbose_name='是否仅针对某一菜进行优惠')
    food_id = models.IntegerField(verbose_name='该食物的id')

    add_time = models.DateTimeField(default=timezone.now, verbose_name='添加时间', help_text='添加时间')

    class Meta:
        verbose_name = '优惠'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name