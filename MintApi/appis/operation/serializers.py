from rest_framework import serializers

from . import models
#

class RatingsSerializer(serializers.ModelSerializer):
    """
        评分
    """
    class Meta:
        model = models.Ratings
        fields = '__all__'
