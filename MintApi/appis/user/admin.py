from django.contrib import admin
from . import models
from MintApi.settings import SITE_CONF

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'bith', 'gender']
    search_fields = ['name', 'phone', 'email']
    list_filter = ['gender']

    list_per_page = SITE_CONF['LIST_PRE_PAGE']
    empty_value_display = SITE_CONF['EMPTY_VALUE_DISPLAY']

class VertifyCodeAdmin(admin.ModelAdmin):
    list_display = ['phone', 'result']
    list_per_page = SITE_CONF['LIST_PRE_PAGE']
    empty_value_display = SITE_CONF['EMPTY_VALUE_DISPLAY']

admin.site.register(models.UserProfile, UserAdmin)
admin.site.register(models.VertifyCode, VertifyCodeAdmin)