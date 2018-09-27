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