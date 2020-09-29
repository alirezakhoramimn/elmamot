from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Language, FrameWork

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['about']
    def location(self, item):
        return reverse(item)


class LanguageSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9
    protocol = 'https'

    def items(self):
        return Language.objects.filter(status='published')

    def lastmod(self, obj):
        return obj.publish

class FrameWorkSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.8
    protocol = 'https'

    def items(self):
        return FrameWork.objects.filter(status='published')

    def lastmod(self, obj):
        return obj.publish