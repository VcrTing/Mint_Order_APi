import random

from django.db.models import Q
from django.forms import model_to_dict
from django.http import QueryDict, JsonResponse

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

from rest_framework.response import Response
from rest_framework import mixins, viewsets, permissions, status
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from . import models
from . import serializers
from MintApi.settings import SMS_API_KEY, SMS_WEB_NAME
from extra.utils.captcha import captcha
from extra.utils.sms import yun_pian

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

class SmsCodeViewSet(viewsets.GenericViewSet,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin):
    """
        手机验证码
    """
    queryset = models.SmsCode.objects.all()
    serializer_class = serializers.SmsCodeSerializer
    lookup_field = 'phone'

    def generate_code(self):
        """
        生成验证码
        """
        seeds = '123456789'
        random_str = []
        for i in range(4):
            random_str.append(random.choice(seeds))
        return ''.join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True) # 400 错误

        phone = serializer.validated_data['phone']
        code = self.generate_code()
        print(phone, code)
        yp = yun_pian.YunPian(SMS_API_KEY, SMS_WEB_NAME)
        sms_status =  yp.send_sms(code=code, phone=phone)
        if sms_status['code'] == 0:
            return Response({
                'code': '1',
                'msg': sms_status['msg']
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            code_record = models.SmsCode(code=code, phone=phone)
            code_record.save()
            return Response({
                'code': code
            }, status=status.HTTP_201_CREATED)

class VertifyCodeViewSet(viewsets.GenericViewSet,
                         mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin):
    """
        短信验证码
    """
    queryset = models.VertifyCode.objects.all()
    serializer_class = serializers.VertifyCodeSerializer
    lookup_field = 'username'

    def create(self, request, *args, **kwargs):
        instance = request.data
        result, img_content = captcha.get_captcha()
        instance = QueryDict('result={result}&img_content={img_content}&username={username}'.format(
            result = result, img_content = img_content, username = instance.get('username')))

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

class UsersViewSet(mixins.CreateModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.RetrieveModelMixin,
                         viewsets.GenericViewSet):
    """
        用户图片验证码 方式进入本平台
    """
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_serializer_class(self):
        raise Exception('Here must be implemented!!!')

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
        return self.request.user

class UserRegisterViewSet(UsersViewSet):
    """
        用户图片验证码 方式进入本平台
    """
    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.UserRegisterSerializer
        return serializers.UserDetailSerializer


"""
class LoginViewSet(viewsets.GenericViewSet):
    #    用户 登录/注册 要用 中转模型层
    serializer_class = serializers.UserLoginSerializer
"""