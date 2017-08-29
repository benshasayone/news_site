# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models


class NewsTypes(models.Model):
    """
        Add and store different news types
    """
    type = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = "News Types"

    def __str__(self):  # __unicode__ on Python 2
        return self.type


class News(models.Model):
    """
        Details about News
    """
    authors = models.CharField(max_length=100,default='Anonymous')
    news_type = models.ForeignKey(NewsTypes,related_name='ntypes')
    title = models.CharField(max_length=200)
    content = models.TextField(default='News yet to added')
    uploaded_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/',null=True,blank=True)

    class Meta:
        verbose_name_plural = "News"

    def __str__(self):  # __unicode__ on Python 2
        return self.title