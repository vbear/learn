# coding=utf8
from __future__ import unicode_literals
from product.models import Product
from django.db import models


# Create your models here.

class Apitest(models.Model):
    apitestname = models.CharField('流程接口名称', max_length=64)
    apitestdesc = models.CharField('描述', max_length=64, null=True)
    apitester = models.CharField('测试负责人', max_length=16)
    apitestresult = models.BooleanField('测试结果')
    create_time = models.DateTimeField('创建时间', auto_now=True)

    class Meta:
        verbose_name = '流程场景接口'
        verbose_name_plural = '流程场景接口'

    def __str__(self):
        return self.apitestname


class Apistep(models.Model):
    Apitest = models.ForeignKey(Apitest)
    apiname = models.CharField('接口名称', max_length=100)
    apiurl = models.CharField('url地址', max_length=200)
    apiparamvalue = models.CharField('请求参数和值', max_length=800)
    apiparamvalue = models.CharField('请求参数和值', max_length=800)
    REQUEST_METHOD = (('get', 'get'), ('post', 'post'), ('put', 'put'), ('delete', 'delete'), ('patch', 'patch'))
    apimethod = models.CharField(verbose_name='请求方法', choices=REQUEST_METHOD, default='get', max_length=200, null=True)
    apiresult = models.CharField('预期结果', max_length=200)
    apistatus = models.BooleanField('是否通过')
    create_time = models.DateTimeField('创建时间', auto_now=True)


def __str__(self):
    return self.name
