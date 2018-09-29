from django.db import models
from django.utils import timezone

# Create your models here.

class Location(models.Model):
    """
        根据经纬度获取地理位置信息
    """
    geohash = models.CharField(max_length=120, verbose_name='经度,纬度', help_text='经度,纬度')
    name = models.CharField(max_length=200, verbose_name='显示地址', help_text='显示地址')
    address = models.CharField(max_length=200, verbose_name='地址', help_text='地址')
    city = models.CharField(max_length=60, verbose_name='城市', help_text='城市')
    longitude = models.FloatField(verbose_name='纬度', help_text='纬度')
    latitude = models.FloatField(verbose_name='经度', help_text='经度')

    class Meta:
        verbose_name = '获取位置的接口'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Gategory(models.Model):
    """
        商家种类
    """
    is_in_serving = models.BooleanField(default=True, verbose_name='是否在服务区内', help_text='是否在服务区内')
    image_url = models.ImageField(upload_to='gategory/images', verbose_name='图片', help_text='图片')
    icon_url = models.ImageField(upload_to='gategory/icons', verbose_name='图标', help_text='图标', default="")
    description = models.CharField(max_length=200, verbose_name='描述', help_text='描述')
    title_color = models.CharField(max_length=30, verbose_name='颜色', help_text='颜色', default="")
    title = models.CharField(max_length=60, verbose_name='标题', help_text='标题')
    link = models.URLField(verbose_name='链接', help_text='链接', default="")

    v = models.SmallIntegerField(verbose_name='数据的版本号', help_text='数据的版本号', default=0)
    add_time = models.DateTimeField(default=timezone.now, verbose_name='添加时间', help_text='添加时间')

    class Meta:
        verbose_name = '商家分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

"""
    piecewise_agent_fee {
        tips: 配送费￥5元
    },
"""
class ShopLicense(models.Model):
    """
        商铺审核图片
    """
    catering_service_license_image = models.ImageField(upload_to='shop/service_license_image', verbose_name='营业执照')
    business_license_image = models.ImageField(upload_to='shop/business_license_image', verbose_name='授权执照')

    add_time = models.DateTimeField(default=timezone.now, verbose_name='添加时间', help_text='添加时间')

    class Meta:
        verbose_name = '商铺审核的图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '营业执照等'

class OpeningHours(models.Model):
    """
        营业时间:
            opening_hours [
                '开门时间 - 打烊时间',
            ]
    """
    is_open = models.NullBooleanField(default=True, verbose_name='今天是否营业')
    open_hour = models.CharField(max_length=12, verbose_name='开营时间')
    close_hour = models.CharField(max_length=12, verbose_name='打烊时间')
    description = models.CharField(max_length=120, verbose_name='描述')

    add_time = models.DateTimeField(default=timezone.now, verbose_name='添加时间', help_text='添加时间')

    class Meta:
        verbose_name = '营业时间'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.description

class Activities(models.Model):
    """
        活动
    """
    icon_name = models.CharField(max_length=12, verbose_name='活动icon名称')
    name = models.CharField(max_length=30, verbose_name='活动名称')
    description = models.CharField(max_length=200, verbose_name='描述')
    icon_color = models.CharField(max_length=12, verbose_name='icon颜色')
    _id = models.CharField(max_length=120, verbose_name='活动的id == key')

    add_time = models.DateTimeField(default=timezone.now, verbose_name='添加时间', help_text='添加时间')

    class Meta:
        verbose_name = '店铺活动'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class DeliveryMode(models.Model):
    """
        配送方式
    """
    color = models.CharField(max_length=12, verbose_name='颜色')
    is_solid = models.BooleanField(default=True, verbose_name='是否专送')
    text = models.CharField(max_length=120, verbose_name='内容信息')

    add_time = models.DateTimeField(default=timezone.now, verbose_name='添加时间', help_text='添加时间')

    class Meta:
        verbose_name = '配送方式'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text

class Identification(models.Model):
    """
        商家营业法律信息
    """
    registered_number = models.CharField(max_length=200, verbose_name='工商号')
    registered_address = models.CharField(max_length=200, verbose_name='工商地址')
    operation_period = models.DateField(default=timezone.now, verbose_name='操作时间')
    licenses_scope = models.CharField(max_length=60, verbose_name='授权空间')
    licenses_number = models.CharField(max_length=60, verbose_name='授权号')
    licenses_date = models.DateTimeField(default=timezone.now, verbose_name='授权日期')
    legal_person = models.CharField(max_length=60, verbose_name='法人姓名')
    identificate_date = models.DateTimeField(default=timezone.now, verbose_name='注册日期')
    identificate_agency = models.CharField(max_length=120, verbose_name='注册机构名称')
    company_name = models.CharField(max_length=120, verbose_name='公司名称')

    add_time = models.DateTimeField(default=timezone.now, verbose_name='添加时间', help_text='添加时间')

    class Meta:
        verbose_name = '商家认证信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.company_name

class Supports(models.Model):
    """
        外卖的支持
    """
    description = models.CharField(max_length=120, verbose_name='描述')
    icon_color = models.CharField(max_length=12, verbose_name='颜色')
    icon_name = models.CharField(max_length=12, verbose_name='icon名称')
    name = models.CharField(max_length=60, verbose_name='名称')
    _id = models.CharField(max_length=120, verbose_name='保障的id == key', null=True, blank=True)

    add_time = models.DateTimeField(default=timezone.now, verbose_name='添加时间', help_text='添加时间')

    class Meta:
        verbose_name = '外卖的支持信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Shop(models.Model):
    """
        商家
    """
    name = models.CharField(max_length=120, verbose_name='店家名称')
    address = models.CharField(max_length=200, verbose_name='店家地址')
    latitude = models.FloatField(verbose_name='纬度')
    longitude = models.FloatField(verbose_name='经度')
    phone = models.CharField(max_length=60, verbose_name='电话')
    category = models.OneToOneField(Gategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='种类')
    status = models.SmallIntegerField(verbose_name='状态', default=1)
    recent_order_num = models.IntegerField(verbose_name='订单数量')
    rating_count = models.FloatField(verbose_name='评分数量')
    rating = models.FloatField(verbose_name='综合评分')
    promotion_info = models.CharField(max_length=120, verbose_name='提示信息')
    is_new = models.BooleanField(default=True, verbose_name='是否是新店')
    is_premium = models.BooleanField(default=False, verbose_name='是否溢价')
    image_path = models.ImageField(upload_to='shop/images', verbose_name='商家图片')
    float_minimum_order_amount = models.FloatField(verbose_name='最小减免')
    float_delivery_fee = models.FloatField(verbose_name='配送费')

    distance = models.CharField(max_length=30, verbose_name='距离', null=True, blank=True)
    order_lead_time = models.CharField(max_length=30, verbose_name='预计送达时间', null=True, blank=True)
    description = models.CharField(max_length=120, verbose_name='描述', null=True, blank=True)

    v = models.SmallIntegerField(verbose_name='数据的版本号', help_text='数据的版本号', default=0)
    add_time = models.DateTimeField(default=timezone.now, verbose_name='添加时间', help_text='添加时间')

    opening_hours = models.ForeignKey(to=OpeningHours, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='营业时间')
    license = models.OneToOneField(to=ShopLicense, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='营业执照等')
    identification = models.OneToOneField(to=Identification, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='审核信息')
    delivery_mode = models.OneToOneField(to=DeliveryMode, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='配送方式')
    activities = models.ForeignKey(to=Activities, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='活动')
    supports = models.ManyToManyField(to=Supports, null=True, blank=True, verbose_name='保障', related_name='+')

    class Meta:
        verbose_name = '商家'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
