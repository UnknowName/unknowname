#!/bin/env python
# coding:utf8


from django.contrib import admin
from portmap.models import ConfigTemplate
from portmap.models import MapDetail


admin.site.register(ConfigTemplate)
admin.site.register(MapDetail)
