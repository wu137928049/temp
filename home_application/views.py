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

#mako模板，可以直接在前端页面编写python代码
from django.http import JsonResponse
from common.mymako import render_mako_context
from django.contrib.auth.hashers import make_password,check_password
from psms.models import Users
import os
import xlrd
import pymysql
#不导入下边这个，不能传中文，很麻烦。
import sys
import time, threading
reload(sys)
sys.setdefaultencoding('utf-8')

#from home_application import models
from psms import models

def login(request):
    #貌似无卵用
    return render_mako_context(request,'psms/login.html')
def home(request,name,template_name):
    icon = models.Users.objects.get(u_name=name).u_icon
    ywx = models.Service_line.objects.filter(favor__u_name=name).values_list()

    #定义要给字典，键是业务名，值是路由，负责的业务对应内容
    dict_yw = {}
    for i in ywx:
        a = i[1]
        a = str(a)
        zyew = models.service_summary.objects.filter(yew=a).values_list()
        if zyew:
            j = zyew[0][1]
            z = zyew[0][2]
            dict_yw[j] = z

    #所有业务线对应内容
    zywx_dict = {}
    zywx_list = models.service_summary.objects.all().values_list()
    for i in zywx_list:
        j = i[1]
        z = i[2]
        zywx_dict[j] = z

    #将已登陆的用户的头像路径保存到session
    icon = str(icon)
    request.session['icon'] = icon

    return render_mako_context(request,template_name,{'name':name,
                                                                       'icon':icon,
                                                                       'dict_yw':dict_yw,
                                                                      'zywx_dict': zywx_dict,
                                                                       })



#添加删除自己负责的业务线
def tjscywx(request):
    #每个登陆的用户只能调整自己的业务。这里只需要获取已登陆的user即可。
    user = request.session['user']
    #获取到用户负责的业务列表,和未负责的列表
    #所有业务的列表
    all_list = []
    all_yw = models.Service_line.objects.all().values_list()
    for i in all_yw:
        a = i[1]
        all_list.append(a)

    #负责的业务的列表
    yw_list = []
    yw = models.Service_line.objects.filter(favor__u_name=user).values_list()
    for i in yw:
        a = i[1]
        yw_list.append(a)

    #不负责的业务的列表
    bfz_list = []
    for i in all_list:
        if i not in yw_list:
            bfz_list.append(i)

    #暂定最大业务数为20，不够的补空
    fzcd = len(yw_list)
    bfzcd = len(bfz_list)
    if fzcd < 20:
        a = 20 - fzcd
        for i in xrange(a):
            yw_list.append(' ')

    if bfzcd < 20:
        a = 20 - bfzcd
        for i in xrange(a):
            bfz_list.append(' ')

    return render_mako_context(request,'home_application/tianjshanc.html',{
        'yw_list':yw_list,
        'bfz_list':bfz_list,
    })


def ajax_sc(request):
    name = request.GET.get('name')
    user = request.session['user']

    user_obj = models.Users.objects.get(u_name=user)
    yw_obj = models.Service_line.objects.filter(u_name=name).all()
    for i in yw_obj:
        i.favor.remove(user_obj)

    data = {
     'a':'删除成功'
    }
    return JsonResponse(data)


def ajax_add(request):
    data = {
        'a':'添加成功'
    }
    user = request.session['user']
    name = request.GET.get('name')
    user_obj = models.Users.objects.get(u_name=user)
    #多对多的键是在service_line类下，而这个yw_obj可以是多个，所以就需要获取到所有，然后遍历一下，从中得出i，就是其中的每一个。
    #为每一个业务对象添加当前选中的用户，即可。
    yw_obj = models.Service_line.objects.filter(u_name=name).all()
    for i in yw_obj:
        i.favor.add(user_obj)
    return JsonResponse(data)

def ajax_check(request):
    name = request.GET.get('name')
    name_message = ' '
    code = '200'
    user_obj = models.Users.objects.filter(u_name=name).values()
    if user_obj:
        name_message = '用户名已存在'
        code = '700'
    if len(name) == 0 or name == '请输入用户名':
        name_message = '请输入用户名'
        code = '700'
    elif len(name) > 6:
        name_message = '用户名最大长度为6'
        code = '700'

    data = {
        'message':name_message,
        'code':code,
            }

    return JsonResponse(data)


def ajax_login(request):
    name = request.GET.get('name')
    password = request.GET.get('password')
    message = ' '
    code = ' '
    if Users.objects.filter(u_name=name).exists():
        user = Users.objects.get(u_name=name)
        if check_password(password, user.u_password):
            code = '200'
        else:
            message = '您的输入有误，请重新输入。'
            code = '700'
    else:
        message = '您的输入有误，请重新输入。'
        code = '700'

    data = {
        'message':message,
        'code':code
    }
    return JsonResponse(data)

def ajax_getuser(request):
    user = request.session['user']
    data = {
        'user':user
    }
    return JsonResponse(data)


