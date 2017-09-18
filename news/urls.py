from django.conf.urls import url, include

from news.views import NewsListView, NewsDetailView, NewsCatView, NewsSearchView, NewsSearchCatView, ContactusView, \
    SubscribeView, ActivateView, ConfirmView1, ConfirmView2

urlpatterns = [
    url(r'^$', NewsListView.as_view(), name='news-list'),
    url(r'^(?P<newstype>\w+)$', NewsCatView.as_view(), name='news-cat-view'),
    url(r'^(?P<newstype>\w+)/(?P<slug>[\w-]+)$', NewsDetailView.as_view(), name='news-details'),
    url(r'^search/$', NewsSearchView.as_view(), name='demo_title_search'),
    url(r'^search2/$', NewsSearchCatView.as_view(), name='demo_title_search2'),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        ActivateView.as_view(), name='activate'),
    url(r'^letter/$', SubscribeView.as_view(), name='signup'),
    url(r'^contact/$', ContactusView.as_view(), name="contactus"),
    url(r'^confirm/$', ConfirmView1.as_view(), name="contact"),
    url(r'^confirm1/$', ConfirmView2.as_view(), name="contact1"),

]
