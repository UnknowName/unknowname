#!/bin/env python
# coding:utf8


from django.db import models
from django_ueditor.models import UEditorField


class Authors(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'文章作者')
    about = UEditorField(
        max_length=1000, width=900, height=600, verbose_name=u'作者简介'
    )
#    toolbars='mini'

    def __unicode__(self):
        return u'{name}'.format(name=self.name)

    class Meta:
        verbose_name_plural = u'作者管理'


class Classifys(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'分类名称')

    def __unicode__(self):
        return u'{name}'.format(name=self.name)

    class Meta:
        verbose_name_plural = u'分类管理'


class Articles(models.Model):
    title = models.CharField(max_length=50, verbose_name=u'文章标题')
    content = UEditorField(
        max_length=1500, width=900, height=600, verbose_name=u'文章内容'
    )
    reads = models.IntegerField(default=0, verbose_name=u'阅读量')
    author = models.ForeignKey(Authors, verbose_name=u'创作者')
    create_date = models.DateField(auto_now_add=True)
    classify = models.ForeignKey(Classifys, verbose_name='文章归类')

    def __unicode__(self):
        return u'{title},{author}'.format(title=self.title, author=self.author)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('blog.views.article', args=[self.classify.name,str(self.id)])

    class Meta:
        verbose_name_plural = u'文章管理'
        ordering = ['-create_date']
