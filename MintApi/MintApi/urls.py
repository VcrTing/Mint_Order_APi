"""MintApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import static, url

from rest_framework import routers
from rest_framework.documentation import include_docs_urls

# Import
# here that import you module
from . import settings
from appis.user import views as user_views
from appis.business import views as business_views
from appis.operation import views as operation_views

# Router
# here setting your rest routers
router = routers.DefaultRouter()
# business
router.register('gategory', business_views.GategoryViewSet)
router.register('shop', business_views.ShopViewSet)
"""
router.register('shop_support', business_views.SupportViewSet)
router.register('shop_activities', business_views.ActivitiesViewSet)
router.register('shop_license', business_views.ShopLicenseViewSet)
router.register('shop_delivery_mode', business_views.DeliveryModeViewSet)
router.register('shop_opening_hours', business_views.OpeningHoursViewSet)
router.register('shop_identification', business_views.IdentificationViewSet)
"""

# operation
router.register('rating', operation_views.RatingsViewSet)

# user
router.register('users', user_views.UserRegisterViewSet)
router.register('captcha', user_views.VertifyCodeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='Mint外卖')),
    re_path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^(?P<version>(v1|v2))/', include(router.urls)),

    #
    re_path(r'^(?P<version>(v1|v2))/location/(?P<geohash>([\w.,]*))', business_views.LocationView.as_view())
]

urlpatterns += static.static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)