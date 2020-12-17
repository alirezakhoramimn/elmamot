from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from language.views import home as home_lang
from language.sitemaps import LanguageSitemap,FrameWorkSitemap

from rest_framework import routers


from django.views.decorators.csrf import csrf_protect, csrf_exempt

from graphene_django.views import GraphQLView
import language.views as lang_views 
router = routers.DefaultRouter()
router.register(r'languages', lang_views.LanguageViewSet)
router.register(r'frameworks', lang_views.FrameWorkViewSet)

sitemaps = {
       'languages': LanguageSitemap(),
       'frameworks': FrameWorkSitemap(),
    }

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('account/', include('account.urls')),
    path('quiz/', include('quiz.urls')),

    # for now we will be using the built in django urls
    path('account/', include('django.contrib.auth.urls')),
    path('', include('language.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
     name='django.contrib.sitemaps.views.sitemap'),

    path('question/', include('quiz.urls')),

    path('graphql/', GraphQLView.as_view(graphiql=True)),
    # Rest 
    path('rest/', include('rest_framework.urls')),

    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

