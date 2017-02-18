#!/bin/env python
#coding:utf8


from django.db import connection
from blog.models import Classifys,Articles


def archive_year(request):
    cursor = connection.cursor()
    cursor.execute('SELECT DISTINCT year(create_date) FROM blog_articles')
    rows = cursor.fetchall()
    years = []
    for row in rows:
        years.append(row[0])
    sorted(years, reverse=True)[:10]
    return {'years':years}


def add_menu(request):
    menus_object = Classifys.objects.all()
    menus = [name.name for name in menus_object]
    return {'menus':menus,'user':request.user}


def hot_articles(request):
    hots = Articles.objects.order_by('-reads')[:5]
    return {'hots':hots}
