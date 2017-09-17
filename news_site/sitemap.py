from django.contrib.sitemaps import Sitemap

from news.models import News, NewsTypes


class news_sitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return News.objects.all()


class category_sitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return NewsTypes.objects.all()
