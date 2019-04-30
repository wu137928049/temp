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

from django.conf.urls import patterns


urlpatterns = patterns(
    'home_application.views',
    (r'^$', 'login'),
    (r'^home/(\w+)/$', 'home',{'template_name':'home_application/home.html'}),
    # (r'^home/(\w+)/$', 'home',{'template_name':'home_application/home.html'}),
    (r'^tjscywx/$', 'tjscywx'),
    (r'^ajax_tjsc/$', 'ajax_tjsc'),
    (r'^ajax_sc/$', 'ajax_sc'),
    (r'^ajax_add/$', 'ajax_add'),
    (r'^ajax_check/$', 'ajax_check'),
    (r'^ajax_login/$', 'ajax_login'),
    (r'^ajax_getuser/$', 'ajax_getuser'),




)
