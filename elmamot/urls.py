"""elmamot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from language.views import home as home_lang
from language.sitemaps import LanguageSitemap,FrameWorkSitemap
<<<<<<< HEAD
from rest_framework import routers
=======

from django.views.decorators.csrf import csrf_protect, csrf_exempt
>>>>>>> 677b20f59146d8d0ae020ad6e985d1bc0cad7ef2
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

<<<<<<< HEAD
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    # Rest 
    path('rest/', include('rest_framework.urls')),
=======
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),

    #path('', TemplateView.as_view(template_name='home.html'), name='home'),
>>>>>>> 677b20f59146d8d0ae020ad6e985d1bc0cad7ef2
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

