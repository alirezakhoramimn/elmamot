from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'language'

urlpatterns = [
    path('langcreate/', views.LangCreateView.as_view(), name= 'lang_create'),
    path('framecreate/', views.FrameCreateView.as_view(), name = 'framecreate'),
    path('', views.home, name='home'),

    path('lang_detail/<str:name>/<int:number>/update', views.LangUpdateView.as_view(), name='lang_update'),
    #path('l/<str:name>/<slug:slug>/', views.lang_post_detail, name='lang_detail'),

    path('lang_detail/<str:name>/<int:number>/', views.lang_post_detail, name='lang_detail'),
    
    path('frame_detail/<str:lang>/<str:name>/<int:number>/', views.frame_post_detail, name='frame_detail'),
    path('frame_detail/<str:lang>/<str:name>/<int:number>/update', views.FrameUpdateView.as_view(), name='frame_detail_update'),

    path('all/', views.all, name='all'),
    # Searching 
    path('search/', views.post_search, name='search_results'),
	]	