from django.shortcuts import render

from rest_framework import mixins, viewsets

from . import models
from . import serializers
# Create your views here.

class RatingsViewSet(viewsets.ModelViewSet):
    """
        评分
    """
    queryset = models.Ratings.objects.all()
    serializer_class = serializers.RatingsSerializer