import datetime

from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework import validators

from . import models

User = get_user_model()
# Your Serializer

class SmsCodeSerializer(serializers.ModelSerializer):
    """
        用户 手机短信验证码
    """
    code = serializers.CharField(max_length=12, read_only=True)
    add_time = serializers.DateTimeField(read_only=True)
    def validate_phone(self, phone):
        """
        验证手机号码
        """
        if User.objects.filter(phone = phone).count():
            raise serializers.ValidationError('用户已存在')

        one_minits_ago = datetime.datetime.now() - datetime.timedelta(hours=0, minutes=1, seconds=0)
        if models.SmsCode.objects.filter(add_time__gt=one_minits_ago, phone=phone):
            raise serializers.ValidationError('距离上一次发送未超过60s')
        return phone

    class Meta:
        model = models.SmsCode
        fields = '__all__'

class VertifyCodeSerializer(serializers.ModelSerializer):
    """
        用户，图片验证码
    """
    result = serializers.CharField(allow_null=True, required=False, write_only=True, help_text='验证码的值，不填')
    img_content = serializers.CharField(allow_null=True, required=False, help_text='验证码的图片地址，不填')
    add_time = serializers.DateTimeField(read_only=True)

    class Meta:
        model = models.VertifyCode
        fields = '__all__'

class UserRegisterBaseSerialzier(serializers.ModelSerializer):
    """
        用户注册的父类
    """
    username = serializers.CharField(required=True, allow_blank=False,
                                     validators=[validators.UniqueValidator(queryset=User.objects.all(), message='用户验证失败')],
                                     help_text='用户名', label='用户名')
    password = serializers.CharField(help_text='密码', label='密码', write_only=True,
                                     style={
                                         'input_type': 'password'
                                     })
    def create(self, validated_data):
        user = super(UserRegisterBaseSerialzier, self).create(validated_data=validated_data)
        user.set_password(validated_data['password']) # 利用内部途径加密 密码
        user.save()
        return user

    def validate_code(self, code):
        raise Exception('Here must be implemented!!!')

class UserRegisterSerializer(UserRegisterBaseSerialzier):
    """
        用户 通过 手机号+验证码 进入本平台
    """
    sms_code = serializers.CharField(max_length=4, min_length=4, label='短信验证码', write_only=True,
                                     error_messages={
                                        'required': '请输入验证码',
                                         'max_length': '验证码为4位数',
                                         'min_length': '验证码为4位数',
                                         'blank': '请输入验证码'
                                     },
                                     help_text='短信验证码')
    captcha_code = serializers.CharField(max_length=4, min_length=4, label='图片验证码', write_only=True,
                                         error_messages={
                                            'required': '请输入图片验证码',
                                             'max_length': '验证码为4位数',
                                             'min_length': '验证码为4位数',
                                             'blank': '请输入图片验证码'
                                         },
                                         help_text='图片验证码')
    def validate_sms_code(self, sms_code):
        verify_records = models.SmsCode.objects.filter(phone=self.initial_data['username']).order_by('-add_time')
        if not verify_records:
            raise serializers.ValidationError('手机验证码错误')
        last_record = verify_records[0]
        if last_record.code != sms_code:
            raise serializers.ValidationError('手机验证码错误')
        return sms_code

    def validate_captcha_code(self, captcha_code):
        verify_records = models.VertifyCode.objects.filter(username=self.initial_data['username']).order_by('-add_time')
        if not verify_records:
            raise serializers.ValidationError('图片验证码错误')
        last_record = verify_records[0]

        captcha_code = captcha_code.lower()
        data_code = last_record.result.lower()
        if data_code != captcha_code:
            raise serializers.ValidationError('图片验证码错误')
        return captcha_code

    def validate(self, attrs):
        attrs['phone'] = attrs['username']
        del attrs['sms_code']
        del attrs['captcha_code']
        return attrs

    class Meta:
        model = User
        fields = ('username', 'password', 'sms_code', 'captcha_code')

class UserDetailSerializer(serializers.ModelSerializer):
    """
        用户信息
    """
    class Meta:
        model = models.UserProfile
        fields = ('name', 'bith', 'phone', 'email', 'gender', 'username')


# 注册的验证码的一些方法
"""
    if verify_records:
        last_record = verify_records[0]
        five_minits_ago = datetime.datetime.now() - datetime.timedelta(hours=0, minutes=5, seconds=0)
        if five_minits_ago > last_record.add_time:
            raise serializers.ValidationError('验证码已经过期')
        if last_record.code != code:
            raise serializers.ValidationError('验证码错误')
    else:
        raise serializers.ValidationError('验证码错误')
"""