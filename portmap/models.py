#!/bin/env pyton
# coding:utf8


from django.db import models


class ConfigTemplate(models.Model):
    template_name = models.CharField(max_length=50, verbose_name=u'模板名称')
    config_str = models.TextField(max_length=6000, verbose_name=u'配置模板')

    def __unicode__(self):
        return "{name}".format(name=self.template_name)


class MapDetail(models.Model):
    APPS = (
        ('web','xueshanai-web'),
        ('app','xueshanai-app'),
        ('mobile','xueshanai-mobile'),
        ('mobile-ssl','xueshanai-mobile-ssl'),
    )
    ips = models.CharField(max_length='150', verbose_name=u'服务器IPs')
    ports = models.CharField(max_length='150', verbose_name=u'服务器PORTs')
    app = models.CharField(
        max_length=30, choices=APPS, verbose_name=u'应用名称'
    )

    def __unicode__(self):
        return "{name},{ip},{port}".format(
            name=self.app,ip=self.ips,port=self.ports
        )


