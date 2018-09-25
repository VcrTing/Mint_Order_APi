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

# Router
# here setting your rest routers
router = routers.DefaultRouter()
router.register('users', user_views.UserRegisterViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='Mint外卖')),
    re_path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(
        r'^(?P<version>(v1|v2))/',
        include(router.urls)
    ),
]

urlpatterns += static.static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)