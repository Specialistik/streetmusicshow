# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.html import format_html
from core.models import MainPage, Photo

from sorl.thumbnail import get_thumbnail


class ModelPhoto(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" width="261" height="150"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'

    list_display = ['image_tag', ]

admin.site.register(MainPage)
admin.site.register(Photo, ModelPhoto)
