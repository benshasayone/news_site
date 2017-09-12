from django.conf.urls import url, include

from news import views
from news.views import NewsListView, NewsDetailView, search, NewsCatView, search123, NewsSearchView, NewsSearchCatView, \
    activate, sub1

urlpatterns = [
    url(r'^$', NewsListView.as_view(), name='news-list'),
    url(r'^(?P<newstype>\w+)$',NewsCatView.as_view(), name='news-cat-view'),
    url(r'^(?P<newstype>\w+)/(?P<slug>[\w-]+)$',NewsDetailView.as_view(), name='news-details'),
    url(r'^new$',views.search),
    url(r'^search/$', NewsSearchView.as_view(), name='demo_title_search'),
    url(r'^search2/$', NewsSearchCatView.as_view(), name='demo_title_search2'),
    url(r'^list/$', search123, name='news-list1'),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
    url(r'^letter/$', sub1, name='signup'),

]

