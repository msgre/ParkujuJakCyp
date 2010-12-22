# -*- coding: utf-8 -*-

from django.contrib import admin
from pjc.photos.models import Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('created', 'ip', )

admin.site.register(Photo, PhotoAdmin)
