#!/bin/env python
# coding:utf8


from portmap.models import ConfigTemplate
from portmap.models import MapDetail


def get_portmap(app_name):
    app_info = MapDetail.objects.get(app=app_name)
    if ',' in app_info.ips and ',' in app_info.ports:
        ip_a,ip_b = app_info.ips.split(',')
        port_a,port_b = app_info.ports.split(',')
        info_a = '{ip}:{port};\n'.format(ip=ip_a,port=port_a)
        info_b = 'server {ip}:{port};\n'.format(ip=ip_b,port=port_b)
        return info_a + info_b
    return "{ip}:{port};".format(ip=app_info.ips, port=app_info.ports)


def create_conf_str(file_name):
    web_info = get_portmap('web')
    mobile_info = get_portmap('mobile')
    app_info = get_portmap('app')
    mobile_ssl_info = get_portmap('mobile-ssl')
    config_str = ConfigTemplate.objects.get(pk=1).config_str  %(
        web_info,mobile_info,app_info,mobile_ssl_info
    )
    try:
        with open(file_name,'w') as f:
            f.write(config_str.replace('\r\n','\n'))
    except Exception as e:
        return e
    return 200


def get_post_data(form_model,req_post):
    form = form_model(req_post)
    if form.is_valid():
        ips = form.cleaned_data.get('ips',None)
        ports = form.cleaned_data.get('ports',None)
        app = form.cleaned_data.get('app_type',None)
        return (app,ips,ports)
