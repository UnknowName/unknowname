#!/bin/env python
# coding:utf8


from django.contrib import admin
from blog.models import Authors, Articles, Classifys
from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = 'django.contrib.auth'
    verbose_name = u'用户与权限系统'


class AdminConfig(AppConfig):
    name = 'django.contrib.admin'
    verbose_name = u'后台管理'


class AuthorsAdmin(admin.ModelAdmin):
#    verbose_name = u'作者管理'
    list_display = ('name',)
#    fields = ('name','about')


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = ('title', 'author', 'classify', 'content')


admin.site.register(Authors, AuthorsAdmin)
admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Classifys)
