# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from news.models import NewsTypes, News, NewsLetter, Contactus


def make_published(modeladmin, request, queryset):
    queryset.update(published=True)
make_published.short_description = "Mark selected news as published"

def make_unpublished(modeladmin, request, queryset):
    queryset.update(published=False)
make_unpublished.short_description = "Mark selected news as unpublished"

def make_subscription(modeladmin, request, queryset):
    queryset.update(subscription=True)
make_subscription.short_description = "Mark selected news as subscribed"

def make_unsubscription(modeladmin, request, queryset):
    queryset.update(subscription=False)
make_unsubscription.short_description = "Mark selected news as unsubscribed"

class AdminImageWidget(AdminFileWidget):
   """
      image display widget for all image display
   """
   def render(self, name, value, attrs=None):
       output = []
       if value and getattr(value, "url", None):
           image_url = value.url
           file_name=str(value)
           output.append(u' <a href="%s" target="_blank"><img src="%s" alt="%s" width="60" width="60"/></a> %s ' % \
               (image_url, image_url, file_name, _('Change:')))
       output.append(super(AdminFileWidget, self).render(name, value, attrs))
       return mark_safe(u''.join(output))

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','authors', 'published']
    actions = [make_published,make_unpublished,make_subscription,make_unsubscription]
    list_filter = ('published', 'subscription')
    search_fields = ['title','authors']
    # readonly_fields = ('image_tag',)

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'image':#Specify the field to be overrided
            request = kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(NewsAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(News, NewsAdmin)
admin.site.register(NewsTypes)
admin.site.register(NewsLetter)
admin.site.register(Contactus)
