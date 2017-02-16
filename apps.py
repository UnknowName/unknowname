#!/bin/env python
# coding:utf8


from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'
    verbose_name = u'博客系统'


class AuthConfig(AppConfig):
    name = 'django.contrib.auth'
    verbose_name = u'用户权限系统'
