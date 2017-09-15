# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from news.models import NewsTypes, News, NewsLetter, Contactus


class NewsAdmin(admin.ModelAdmin):
    pass


admin.site.register(News, NewsAdmin)
admin.site.register(NewsTypes)
admin.site.register(NewsLetter)
admin.site.register(Contactus)