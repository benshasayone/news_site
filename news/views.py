# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q
from django.http import HttpResponse, request
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext, Context
from django.template.loader import get_template
from django.urls import reverse
from django.views.generic import ListView, DetailView, TemplateView

from news.models import News, NewsTypes


class NewsListView(ListView):

    model = News
    template_name = 'news_list.html'
    paginate_by = 4
    context_object_name = 'news'
    queryset = News.objects.all().order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super(NewsListView, self).get_context_data(**kwargs)
        context['news_cat_list'] = NewsTypes.objects.all()
        return context

    def get_absolute_url(self):
        return reverse('news-detail', args=[str(self.id)])


class NewsDetailView(DetailView):
    """
    To display News in detail
    """
    model = News
    template_name = 'news_details.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        get_slug = self.kwargs['slug']
        context['news_cat_list'] = NewsTypes.objects.all()
        context['news_det'] = News.objects.get(slug=get_slug)
        return context



def search(request):
    return render(request, 's.html')


class NewsCatView(ListView):
    """
        To display News in category
    """
    model = News
    template_name = 'news_cat.html'
    paginate_by = 2
    context_object_name = 'news'

    def get_queryset(self,**kwargs):
        ntype = self.kwargs['newstype']
        return News.objects.filter(news_type__type=ntype).order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super(NewsCatView, self).get_context_data(**kwargs)
        ntype = self.kwargs['newstype']
        context['news_cat_list'] = NewsTypes.objects.all()
        context['type1'] =ntype
        return context




def search123(request):
    return render(request, 'news_list2.html')



class NewsSearchView(ListView):
    model = News
    template_name = 'results.html'
    context_object_name = 'results'

    def get_queryset(self, **kwargs):
        if self.request.is_ajax():
            q = self.request.GET.get('q')
            if q is not None:
                return News.objects.filter(
                    Q(title__contains=q) |
                    Q(content__contains=q)).order_by('-pub_date')



class NewsSearchCatView(ListView):
    model = News
    template_name = 'results.html'
    context_object_name = 'results'

    def get_queryset(self, **kwargs):
        if self.request.is_ajax():
            q = self.request.GET.get('q')
            w = self.request.GET.get('w')
            if q is not None:
                return News.objects.filter(news_type__type = w ).filter(
                    Q(title__contains=q) |
                    Q(content__contains=q)).order_by('-pub_date')




