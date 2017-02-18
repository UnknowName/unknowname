#!/bin/env python
# coding:utf8


from django.shortcuts import render, HttpResponse
from paginator import split_page
from blog.models import Authors, Articles, Classifys
import time


def index(request):
    contacts = Articles.objects.all()
    articles = split_page(request,contacts)
    return render(request, 'index.html', locals())


def about(request):
    return render(request, 'about.html')


def archive(request, year=None):
    now_year = time.gmtime().tm_year
    year = int(year) if int(year) < now_year else now_year
    articles = Articles.objects.filter(create_date__year=year)
    articles = split_page(request,articles)
    return render(request, 'archive.html', locals())


def classify(request, classify=None):
    try:
        articles = Classifys.objects.get(name=classify).articles_set.all()
        articles = split_page(request,articles)
    except Exception:
        return HttpResponse('暂无该分类文章')
    if not articles:
        return HttpResponse('该栏目下暂无相关文章')
    return render(request, 'list.html', locals())


def article(request, classify, id):
    try:
        article = Articles.objects.get(pk=id)
        article.reads += 1
        article.save()
    except Exception:
        return HttpResponse('Sorry,您查看的文章未找到')
    return render(request, 'article_detail.html', locals())
