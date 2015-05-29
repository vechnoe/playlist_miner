#  coding: utf-8

from django.contrib import admin
from core.models import Radiostation, Song, Airplay


admin.site.register(Radiostation)
admin.site.register(Song)
admin.site.register(Airplay)
