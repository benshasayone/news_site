# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe


class NewsTypes(models.Model):
    """
        Add and store different news types
    """
    type = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = "News Types"

    def __str__(self):
        return self.type




class News(models.Model):
    """
        Details about News
    """
    authors = models.CharField(max_length=100, default='Anonymous')
    news_type = models.ForeignKey(NewsTypes, related_name='ntypes')
    title = models.CharField(max_length=200)
    content = models.TextField(default='News yet to added')
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    slug = AutoSlugField(populate_from='title',
                         unique_with=['title'],
                         unique=True, always_update=True)
    published = models.BooleanField(default=False)
    subscription = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "News"

    def get_absolute_url(self):
        return reverse('news:news-details', kwargs={'slug': self.slug, 'newstype': self.news_type.type})

    def __str__(self):
        return self.title

    # def image_tag(self):
    #     if self.image:
    #         return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.image))
    #     else:
    #         pass
    #
    #
    # image_tag.short_description = 'Image'


class NewsLetter(models.Model):
    email = models.EmailField()
    token = models.CharField(max_length=40, default='123456789')
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "NewsLetter"


class Contactus(models.Model):
    name = models.CharField(max_length=100, default='Anonymous')
    email = models.EmailField()
    subject = models.CharField(max_length=40)
    message = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
