"""news_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap

from news.views import my_custom_page_not_found_view
from news_site import settings
from news_site.sitemap import news_sitemap, category_sitemap

handler404 = my_custom_page_not_found_view.as_view()

sitemaps = {
    'news': news_sitemap, 'category': category_sitemap,
}

urlpatterns = [
                  url(r'^pages/', include('django.contrib.flatpages.urls')),
                  url(r'^nc-admin/', admin.site.urls),
                  url(r'^', include('news.urls', namespace='news')),
                  url(r'^accounts/', include('allauth.urls')),

                  url(r'^account/', include('accounts.urls')),
                  url(r'^comments/', include('django_comments.urls')),
                  url(r'^pages/', include('django.contrib.flatpages.urls')),
                  url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
                      name='django.contrib.sitemaps.views.sitemap'),
                  url(r'^robots\.txt$', include('robots.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
