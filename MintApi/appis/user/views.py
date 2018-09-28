from django.db.models import Q
from django.forms import model_to_dict
from django.http import QueryDict, JsonResponse
from django.shortcuts import render

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

from rest_framework.response import Response
from rest_framework import mixins, viewsets, permissions, status
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from . import models
from . import serializers
from extra.utils.captcha import captcha

User = get_user_model()
class CustomBackend(ModelBackend):
    """
        自定义用户验证
    """
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username = username)|Q(phone=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None
# Create your views here.

class VertifyCodeViewSet(viewsets.GenericViewSet,
                         mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.ListModelMixin):
    """
        验证码
    """
    queryset = models.VertifyCode.objects.all()
    serializer_class = serializers.VertifyCodeSerializer
    lookup_field = 'phone'

    def create(self, request, *args, **kwargs):
        instance = request.data
        result, img_content = captcha.get_captcha()
        instance = QueryDict('result={result}&img_content={img_content}&phone={phone}'.format(
            result = result, img_content = img_content, phone = instance.get('phone')))

        serializer = self.get_serializer(data=instance)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        ret = {}
        instance = self.get_object()
        ret['code'] = status.HTTP_200_OK
        ret['data'] = model_to_dict(instance)
        return JsonResponse(ret)

class UserRegisterViewSet(mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    """
        用户注册
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserRegisterSerializer
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_permissions(self):
        if self.action == 'retrieve':
            return [permissions.IsAuthenticated()]
        return [ ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = self.perform_create(serializer)

        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict['token'] = jwt_encode_handler(payload)
        re_dict['name'] = user.name if user.name else user.username

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers = headers)

    def perform_create(self, serializer):
        return serializer.save()

    def get_object(self):
        """
            retrieve 与 delete会用到 id
            不管 id 传任何数字，都得到的是当前的用户
        """
        return self.request.user