# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('template_name', models.CharField(max_length=50, verbose_name='\u6a21\u677f\u540d\u79f0')),
                ('config_str', models.TextField(max_length=6000, verbose_name='\u914d\u7f6e\u6a21\u677f')),
            ],
        ),
        migrations.CreateModel(
            name='MapDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ips', models.CharField(max_length=b'150', verbose_name='\u670d\u52a1\u5668IPs')),
                ('ports', models.CharField(max_length=b'150', verbose_name='\u670d\u52a1\u5668PORTs')),
                ('app', models.CharField(max_length=30, verbose_name='\u5e94\u7528\u540d\u79f0', choices=[(b'web', b'xueshanai-web'), (b'app', b'xueshanai-app'), (b'mobile', b'xueshanai-mobile'), (b'mobile-ssl', b'xueshanai-mobile-ssl')])),
            ],
        ),
    ]
