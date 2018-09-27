from django.contrib import admin

from . import models
from MintApi.settings import SITE_CONF
# Register your models here.

class GategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'title_color', 'description', 'is_in_serving', 'v', 'add_time']
    list_filter = ['is_in_serving', ]
    list_per_page = SITE_CONF['LIST_PRE_PAGE']
    empty_value_display = SITE_CONF['EMPTY_VALUE_DISPLAY']

class ShopLicenseAdmin(admin.ModelAdmin):
    list_display = ['catering_service_license_image', 'business_license_image']
    list_per_page = SITE_CONF['LIST_PRE_PAGE']
    empty_value_display = SITE_CONF['EMPTY_VALUE_DISPLAY']

class OpeningHoursAdmin(admin.ModelAdmin):
    list_display = ['is_open', 'open_hour', 'close_hour', 'description']
    list_filter = ['open_hour', 'close_hour']
    list_per_page = SITE_CONF['LIST_PRE_PAGE']
    empty_value_display = SITE_CONF['EMPTY_VALUE_DISPLAY']

class ActivitiesAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon_name', 'description', 'icon_color', '_id']
    search_fields = ['name', '_id']
    list_per_page = SITE_CONF['LIST_PRE_PAGE']
    empty_value_display = SITE_CONF['EMPTY_VALUE_DISPLAY']

class DelieryModeAdmin(admin.ModelAdmin):
    list_display = ['color', 'is_solid', 'text']
    list_per_page = SITE_CONF['LIST_PRE_PAGE']
    empty_value_display = SITE_CONF['EMPTY_VALUE_DISPLAY']

class IdentificationAdmin(admin.ModelAdmin):
    search_fields = ['company_name', 'identificate_agency']
    list_per_page = SITE_CONF['LIST_PRE_PAGE']
    empty_value_display = SITE_CONF['EMPTY_VALUE_DISPLAY']

class SupportsAdmin(admin.ModelAdmin):
    list_display = ['description', 'name', 'icon_name', 'icon_color']
    search_fields = ['name', 'description']
    list_per_page = SITE_CONF['LIST_PRE_PAGE']
    empty_value_display = SITE_CONF['EMPTY_VALUE_DISPLAY']

class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'recent_order_num', 'rating_count', 'promotion_info', 'is_new', 'float_delivery_fee']
    list_filter = ['is_new', ]
    search_fields = ['name', 'phone']
    list_per_page = SITE_CONF['LIST_PRE_PAGE']
    empty_value_display = SITE_CONF['EMPTY_VALUE_DISPLAY']

admin.site.register(models.Gategory, GategoryAdmin)
admin.site.register(models.ShopLicense, ShopLicenseAdmin)
admin.site.register(models.Supports, SupportsAdmin)
admin.site.register(models.Shop, ShopAdmin)
admin.site.register(models.DeliveryMode, DelieryModeAdmin)
admin.site.register(models.Identification, IdentificationAdmin)
admin.site.register(models.OpeningHours, OpeningHoursAdmin)
admin.site.register(models.Activities, ActivitiesAdmin)