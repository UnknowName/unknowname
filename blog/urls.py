"""unknowname URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url


urlpatterns = [
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^about/$', 'blog.views.about', name='about'),
    url(r'^archive/(?P<year>\d{4})$', 'blog.views.archive', name='archive'),
    url(r'(?P<classify>\w{5,10})/(?P<id>\d{1,4})$', 'blog.views.article', name='article'),
    url(r'(?P<classify>\w{5,10})/list$', 'blog.views.classify', name='classify'),
]
