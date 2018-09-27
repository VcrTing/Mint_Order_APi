from django.contrib import admin

from . import models
from MintApi.settings import SITE_CONF
# Register your models here.

class RatingsAdmin(admin.ModelAdmin):
    list_per_page = SITE_CONF['LIST_PRE_PAGE']
    empty_value_display = SITE_CONF['EMPTY_VALUE_DISPLAY']

admin.site.register(models.Ratings, RatingsAdmin)