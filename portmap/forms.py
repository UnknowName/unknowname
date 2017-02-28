#!/bin/env python
#coding:utf8


from django import forms


class ServerForm(forms.Form):
    APP_TYPES = (
            ('web','xueshandai-web'),
            ('mobile','xueshandai-mobile'),
            ('mobile-ssl','xueshandai-mobile-ssl'),
            ('app','xueshandai-app'),
    )
    ips = forms.CharField(
            label=u'服务器地址', error_messages={'required':u'必须项'},
            widget=forms.TextInput(attrs={'placeholder':'服务器IP地址。多个以,分隔'})
    )
    ports = forms.CharField(max_length=50, label=u'服务器端口',
            widget=forms.TextInput(attrs={'placeholder':'服务器端口。多个以,分隔'})
    )
    app_type = forms.ChoiceField(choices=APP_TYPES, label=u'应用类型')
