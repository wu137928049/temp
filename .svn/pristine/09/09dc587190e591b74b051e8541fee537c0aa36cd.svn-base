# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""
'''
from django.db import models

class  Staff(models.Model):
    colors = models.CharField(max_length=10)


class Colors(models.Model):
    colors = models.CharField(max_length=10)  # 蓝色

    def __str__(self):
        return self.colors


class Ball(models.Model):
    color = models.OneToOneField("Colors")  # 与颜色表为一对一，颜色表为母表
    description = models.CharField(max_length=10)  # 描述

    def __str__(self):
        return self.description


class Clothes(models.Model):
    color = models.ForeignKey("Colors")  # 与颜色表为外键，颜色表为母表
    description = models.CharField(max_length=10)  # 描述

    def __str__(self):
        return self.description


#class Child(models.Model):
 #   sex_choice = ((0, "男"), (1, "女"))
  #  name = models.CharField(max_length=10)  # 姓名
   # favor = models.ManyToManyField('Colors')  # 与颜色表为多对多
    #sex = models.IntegerField(choices=sex_choice, default=0)

class Child(models.Model):
    sex_choice=((0,"男"),(1,"女"))
    name=models.CharField(max_length=10)  #姓名
    favor=models.ManyToManyField('Colors')    #与颜色表为多对多
    sex=models.IntegerField(choices=sex_choice,default=0,null=True) #这里的默认值是使用代码新建数据的时候才生效

    #打印对象会返回他的名字，但是不表示这一直接拿着用。
    def __unicode__(self):
        return self.name
'''