from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import mixins, viewsets, views, status
from rest_framework.response import Response

from . import serializers
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
            location.geohash = geohash
            location.name = location.address + result['sematic_description']

            serializer = serializers.LocationSerializer(location, many=False)
            ret['code'] = status.HTTP_200_OK
            ret['data'] = serializer.data
        except Exception as e:
            ret['data'] = e
        return Response(ret)
