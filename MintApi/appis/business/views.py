
from django_filters.rest_framework.backends import DjangoFilterBackend

from rest_framework import mixins, viewsets, views, status
from rest_framework.response import Response
from rest_framework import filters

from . import serializers
from . import filters as business_filters
from . import models
from extra.utils.location import addr

# Create your views here.
class LocationView(views.APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        geohash = kwargs['geohash']
        ret = {
            'code': status.HTTP_400_BAD_REQUEST,
            'data': None
        }
        try:
            addr_baidu = addr.AddrBaidu(geohash)
            result = addr_baidu.get_addr_dict()
            location = models.Location()
            location.address = result['formatted_address']
            location.latitude = result['location']['lat']
            location.longitude = result['location']['lng']
            location.city = '上海市'
            location.geohash = geohash
            location.name = location.address + result['sematic_description']

            serializer = serializers.LocationSerializer(location, many=False)
            ret['code'] = status.HTTP_200_OK
            ret['data'] = serializer.data
        except Exception as e:
            ret['data'] = e
        return Response(ret)

class GategoryViewSet(viewsets.ModelViewSet):
    """
        商铺种类
    """
    queryset = models.Gategory.objects.all()
    serializer_class = serializers.GategorySerializer

class ShopViewSet(viewsets.ModelViewSet):
    """
        商家
    """
    queryset = models.Shop.objects.all()
    serializer_class = serializers.ShopSerializer

    filter_class = business_filters.ShopFilter
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name', 'address', )
    ordering_fields = ('add_time', 'recent_order_num')

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        for q in queryset:
            q.distance = '1010.3公里'
            q.order_lead_time = '37分钟'
            q.description = '这里是一些描述'

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class SupportViewSet(viewsets.ModelViewSet):
    """
        保障
    """
    queryset = models.Supports.objects.all()
    serializer_class = serializers.SupportsSerializer

class ActivitiesViewSet(viewsets.ModelViewSet):
    """
        活动
    """
    queryset = models.Activities.objects.all()
    serializer_class = serializers.ActivitesSerializer

class DeliveryModeViewSet(viewsets.ModelViewSet):
    """
        配送方式
    """
    queryset = models.DeliveryMode.objects.all()
    serializer_class = serializers.DeliveryModeSerializer

class IdentificationViewSet(viewsets.ModelViewSet):
    """
        营业资料
    """
    queryset = models.Identification.objects.all()
    serializer_class = serializers.IdentificationSerializer

class ShopLicenseViewSet(viewsets.ModelViewSet):
    """
        营业执照
    """
    queryset = models.ShopLicense.objects.all()
    serializer_class = serializers.ShopLicenseSerializer

class OpeningHoursViewSet(viewsets.ModelViewSet):
    """
        营业时间
    """
    queryset = models.OpeningHours.objects.all()
    serializer_class = serializers.OpeningHoursSerializer
