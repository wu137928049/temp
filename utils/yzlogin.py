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


from django.http import HttpResponseRedirect, HttpResponse
from psms.models import Users
#由于这个版本没有mixin类
class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


class CountAddstu(MiddlewareMixin):
    def process_request(self, request):
        # 统一验证登录
        # return none 或者 不写return才会继续往下执行, 不需要执行
        if request.path == '/psms/login/' or request.path == '/psms/regist/' or request.is_ajax():
            return None
        ticket = request.COOKIES.get('ticket')
        if not ticket:
            return HttpResponseRedirect('/psms/login/')

        users = Users.objects.filter(u_ticket=ticket)
        if not users:
            return HttpResponseRedirect('/psms/login/')
# 将user赋值在request请求的user上，以后可以直接判断user有没有存在
# 备注，django自带的有user值
        request.user = users[0].u_name

    def process_exception(self,request,exception):
        #只要有异常报错，就会执行退出，然后提示服务器正在维护，然后给用户发短信，这里是模拟，只创建一个error列表。
        response = HttpResponse('网络故障。。。')
        # 删除cookie
        response.delete_cookie('ticket')
        # 清除session
        try:
            del request.session['user']
        except:
            pass
        return response




