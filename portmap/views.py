#!/usr/bin/env python
# coding:utf8


from django.shortcuts import render
from django.http import HttpResponse
from portmap.models import MapDetail
from portmap.services import create_conf_str,get_post_data
from portmap.forms import ServerForm


def index(request):
    form_html = ServerForm() 
    servers = MapDetail.objects.all()
    return render(request,'index.html',locals())


def update(request):
    if request.method == 'POST':
        app,ip,port = get_post_data(ServerForm, request.POST)
        try:
            MapDetail.objects.filter(app=app).update(ips=ip, ports=port)
            status = create_conf_str('/home/cheng/nginx.conf')
            if status == 200:
                return HttpResponse(u'修改成功<a href="/">返回</a>')
        except Exception as e:
            return HttpResponse(e)
