from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework import validators

from . import models

User = get_user_model()
# Your Serializer

class VertifyCodeSerializer(serializers.ModelSerializer):
    """
        用户，验证码
    """
    result = serializers.CharField(allow_null=True, required=False, write_only=True, help_text='验证码的值，不填')
    img_content = serializers.CharField(allow_null=True, required=False, help_text='验证码的图片地址，不填')
    add_time = serializers.DateTimeField(read_only=True)

    class Meta:
        model = models.VertifyCode
        fields = '__all__'

class UserRegisterSerializer(serializers.ModelSerializer):
    """
        用户
        序列类
    """
    username = serializers.CharField(required=True, allow_blank=False,
                                 validators=[validators.UniqueValidator(queryset=User.objects.all(), message='用户验证失败')],
                                 help_text='用户名', label='用户名')
    password = serializers.CharField(help_text='密码', label='密码', write_only=True,
                                     style={
                                         'input_type': 'password'
                                     })
    def create(self, validated_data):
        user = super(UserRegisterSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate(self, attrs):
        attrs['phone'] = attrs['username']
        print('attr =', attrs)
        # del attrs['code']
        return attrs

    class Meta:
        model = User
        fields = ('username', 'password')