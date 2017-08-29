# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, DetailView

from news.models import News, NewsTypes


class NewsListView(ListView):

    model = News
    template_name = 'news_list.html'

    def get_context_data(self, **kwargs):
        context = super(NewsListView, self).get_context_data(**kwargs)
        context['news_list'] = News.objects.all().order_by('-uploaded_on')[:5]
        context['news_cat_list'] = NewsTypes.objects.all()
        return context

    def get_absolute_url(self):
        return reverse('news-detail', args=[str(self.id)])

class NewsDetailView(DetailView):
    model = News
    template_name = 'news_details.html'
    context_object_name = 'news'
    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context['news_cat_list'] = NewsTypes.objects.all()
        return context


def search(request):
    return render(request, 's.html')

class NewsCatView(ListView):

    model = News
    template_name = 'news_cat.html'

    def get_context_data(self, **kwargs):
        context = super(NewsCatView, self).get_context_data(**kwargs)
        ntype = self.kwargs['newstype']
        context['news_cat'] = News.objects.filter(news_type__type=ntype)
        context['news_cat_list'] = NewsTypes.objects.all()
        return context

