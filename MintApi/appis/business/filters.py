import django_filters
from django.db.models import Q
from django_filters import rest_framework as filters

from . import models
from MintApi.settings import SITE_CONF

class ShopFilter(filters.FilterSet):
    """
        过滤商家
    """
    keyword = django_filters.CharFilter(method='search_by_keyword', help_text='关键字（店名/地址）')
    geohash = django_filters.CharFilter(method='search_by_geohash', help_text='附近的（纬度, 经度）')

    class Meta:
        model = models.Shop
        fields = ['keyword', 'geohash']

    def search_by_keyword(self, queryset, name, value):
        queryset = queryset.filter(Q(name__icontains = value) |
                                   Q(address__icontains=value)
                                   )
        return queryset

    def search_by_geohash(self, queryset, name, value):
        value = value.split(',')
        lat = float(value[0])
        lng = float(value[1])
        queryset = queryset.filter(
            (
                Q(latitude__gt = lat - SITE_CONF['NEARBY_RATE_LAT']) &
                Q(latitude__lt = lat + SITE_CONF['NEARBY_RATE_LAT'])
            ) |
            (
                Q(longitude__gt = lng - SITE_CONF['NEARBY_RATE_LNG']) &
                Q(longitude__lt = lng + SITE_CONF['NEARBY_RATE_LNG'])
            )
        )
        return queryset