from rest_framework import serializers

from . import models
# ser of mine

class LocationSerializer(serializers.ModelSerializer):
    """
        根据经纬度获取地址
    """
    class Meta:
        model = models.Location
        fields = '__all__'

class GategorySerializer(serializers.ModelSerializer):
    """
        商家分类
    """
    add_time = serializers.DateTimeField(read_only=True)
    title_color = serializers.CharField(read_only=True)
    icon_url = serializers.ImageField(read_only=True)
    link = serializers.URLField(read_only=True)
    class Meta:
        model = models.Gategory
        fields = ('is_in_serving', 'image_url', 'icon_url', 'description', 'title_color', 'title', 'link', 'v', 'add_time')

class ShopLicenseSerializer(serializers.ModelSerializer):
    """
        审核资料
    """
    class Meta:
        model = models.ShopLicense
        fields = '__all__'

class SupportsSerializer(serializers.ModelSerializer):
    """
        保障
    """
    class Meta:
        model = models.Supports
        fields = '__all__'

class ActivitesSerializer(serializers.ModelSerializer):
    """
        活动
    """
    class Meta:
        model = models.Activities
        fields = '__all__'

class DeliveryModeSerializer(serializers.ModelSerializer):
    """
        配送方式
    """
    class Meta:
        model = models.DeliveryMode
        fields = '__all__'

class IdentificationSerializer(serializers.ModelSerializer):
    """
        审核信息
    """
    class Meta:
        model = models.Identification
        fields = '__all__'

class OpeningHoursSerializer(serializers.ModelSerializer):
    """
        营业时间
    """
    class Meta:
        model = models.OpeningHours
        fields = '__all__'

class ShopSerializer(serializers.ModelSerializer):
    """
        商店
    """
    supports = SupportsSerializer()
    license = ShopLicenseSerializer()
    activities = ActivitesSerializer()
    delivery_mode = DeliveryModeSerializer()
    opening_hours = OpeningHoursSerializer()
    identification = IdentificationSerializer()

    location = serializers.SerializerMethodField()

    class Meta:
        model = models.Shop
        fields = '__all__'

    def get_location(self, shop):
        return [ shop.latitude, shop.longitude ]

