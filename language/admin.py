# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Language, FrameWork, CommentLanguage, CommentFrameWork
# Register your models here
# Check these https://dev.to/coderasha/how-to-track-number-of-hits-views-for-chosen-objects-in-django-django-packages-series-2-3bcb
# https://pypi.org/project/django-user-tracking/

@admin.register(CommentFrameWork)
class CommentFrameWorkInline(admin.ModelAdmin):
    list_display = ('author','body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('author', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

@admin.register(CommentLanguage)
class CommentLanguageInline(admin.ModelAdmin):
    list_display = ('author','body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('author', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):

    list_display = ('author_username','name','title', 'status')
    list_filter = ('name',)
    #prepopulated_fields = {"slug": ("title",)}

    search_fields = ('description', 'title')
    date_hierarchy = 'created'

    
@admin.register(FrameWork)
class FrameWorkAdmin(admin.ModelAdmin):
    search_fields = ('description', 'title')
