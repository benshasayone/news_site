from django.conf.urls import url

from news import views
from news.views import NewsListView, NewsDetailView, search, NewsCatView

urlpatterns = [
    url(r'^$', NewsListView.as_view(), name='news-list'),
    url(r'^(?P<pk>\d+)$',NewsDetailView.as_view(), name='news-details'),
    url(r'^new$',views.search),
    url(r'^(?P<newstype>\w+)$',NewsCatView.as_view(), name='news-cat-view'),
]

