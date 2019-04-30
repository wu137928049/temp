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


from django.shortcuts import render
from common.mymako import render_mako_context
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import xlrd
from psms.views import sdm_zh
from psms.views import smc_zh
from psms.views import zh_bf
from psms.views import zh_int
from psms.views import qfw
from psms.views import foo
from psms.views import foo_bian
from psms.views import ten
from psms.views import ten_biao
from psms.views import ten_pj_and_sum


#gprs_path = r'C:\\Users\\wu\\Desktop\\zsxq\\gprs.xlsx'
gprs_path = '/data/filelist/gprs.xlsx'
gprs_data = xlrd.open_workbook(gprs_path)


def gprs(request):

    tables = gprs_data.sheets()[0]
    table1 = gprs_data.sheets()[1]
    table2 = gprs_data.sheets()[2]
    table3 = gprs_data.sheets()[3]
    table4 = gprs_data.sheets()[4]
    table5 = gprs_data.sheets()[5]


    # sum_list sum的列表
    one_sum_1 = tables.row_values(4)[3]
    one_sum_10 = tables.row_values(7)[3]
    two_sum_1 = tables.row_values(10)[3]
    two_sum_10 = tables.row_values(13)[3]
    three_sum_1 = tables.row_values(16)[3]
    three_sum_10 = tables.row_values(19)[3]
    fore_sum_1 = tables.row_values(22)[3]
    fore_sum_10 = tables.row_values(25)[3]
    five_sum_1 = tables.row_values(28)[3]
    five_sum_10 = tables.row_values(31)[3]


    # 标题
    one_1 = tables.row_values(3)[4:14]
    two_1 = tables.row_values(4)[4:14]

    one = []
    two = []

    if one_1[0] == ' ':
        for i in xrange(10):
            one.append(' ')
            two.append(' ')
    else:
        one_dict = {}
        for i in xrange(10):
            if one_1[i] != ' ':
                one_dict[one_1[i]] = two_1[i]
        one_dict = sorted(one_dict.items(), key=lambda x: abs(x[1]), reverse=True)

        for i in one_dict:
            a = sdm_zh(i[0])
            one.append(a)
            two.append(i[1])

        if two[0] == ' ':
            two = []
        two = zh_bf(two)

        if len(one) < 10:
            q_cd = 10 - len(one)
            for i in xrange(q_cd):
                one.append(' ')
                two.append(' ')
        if len(one) > 10:
            d_cd = len(one) - 10
            for i in xrange(d_cd):
                one.pop()
                two.pop()

    three_1 = tables.row_values(6)[4:14]
    fore_1 = tables.row_values(7)[4:14]

    three = []
    fore = []
    if three_1[0] == ' ':
        for i in xrange(10):
            three.append(' ')
            fore.append(' ')
    else:
        three_dict = {}
        for i in xrange(10):
            if three_1[i] != ' ':
                three_dict[three_1[i]] = fore_1[i]
        three_dict = sorted(three_dict.items(), key=lambda x: abs(x[1]), reverse=True)

        for i in three_dict:
            a = sdm_zh(i[0])
            three.append(a)
            fore.append(i[1])

        # 将小数转为百分数
        if fore[0] == ' ':
            fore = []
        fore = zh_bf(fore)

        if len(three) < 10:
            q_cd = 10 - len(three)
            for i in xrange(q_cd):
                three.append(' ')
                fore.append(' ')
        if len(three) > 10:
            d_cd = len(three) - 10
            for i in xrange(d_cd):
                three.pop()
                fore.pop()

    wu_1 = tables.row_values(9)[4:14]
    liu_1 = tables.row_values(10)[4:14]
    wu = []
    liu = []
    if wu_1[0] == ' ':
        for i in xrange(10):
            wu.append(' ')
            liu.append(' ')
    else:
        wu_dict = {}
        for i in xrange(10):
            if wu_1[i] != ' ':
                wu_dict[wu_1[i]] = liu_1[i]
        wu_dict = sorted(wu_dict.items(), key=lambda x: abs(x[1]), reverse=True)

        for i in wu_dict:
            a = sdm_zh(i[0])
            wu.append(a)
            liu.append(i[1])

        if liu[0] == ' ':
            liu = []
        liu = zh_bf(liu)

        if len(wu) < 10:
            q_cd = 10 - len(wu)
            for i in xrange(q_cd):
                wu.append(' ')
                liu.append(' ')
        if len(wu) > 10:
            d_cd = len(wu) - 10
            for i in xrange(d_cd):
                wu.pop()
                liu.pop()

    qi_1 = tables.row_values(12)[4:14]
    ba_1 = tables.row_values(13)[4:14]
    qi = []
    ba = []
    if qi_1[0] == ' ':
        for i in xrange(10):
            qi.append(' ')
            ba.append(' ')
    else:
        qi_dict = {}
        for i in xrange(10):
            if qi_1[i] != ' ':
                qi_dict[qi_1[i]] = ba_1[i]
        qi_dict = sorted(qi_dict.items(), key=lambda x: abs(x[1]), reverse=True)

        for i in qi_dict:
            a = sdm_zh(i[0])
            qi.append(a)
            ba.append(i[1])

        if ba[0] == ' ':
            ba = []
        ba = zh_bf(ba)

        if len(qi) < 10:
            q_cd = 10 - len(qi)
            for i in xrange(q_cd):
                qi.append(' ')
                ba.append(' ')
        if len(qi) > 10:
            d_cd = len(qi) - 10
            for i in xrange(d_cd):
                qi.pop()
                ba.pop()

    cuo_one_1 = tables.row_values(15)[4:14]
    cuo_two_1 = tables.row_values(16)[4:14]
    cuo_one = []
    cuo_two = []
    if cuo_one_1[0] == ' ':
        for i in xrange(10):
            cuo_one.append(' ')
            cuo_two.append(' ')
    else:

        cuo_one_dict = {}
        for i in xrange(10):
            if cuo_one_1[i] != ' ':
                cuo_one_dict[cuo_one_1[i]] = cuo_two_1[i]
        cuo_one_dict = sorted(cuo_one_dict.items(), key=lambda x: abs(x[1]), reverse=True)

        for i in cuo_one_dict:
            cuo_one.append(i[0])
            cuo_two.append(i[1])

        if cuo_two[0] == ' ':
            cuo_two = []
        cuo_two = zh_bf(cuo_two)

        if len(cuo_one) < 10:
            q_cd = 10 - len(cuo_one)
            for i in xrange(q_cd):
                cuo_one.append(' ')
                cuo_two.append(' ')
        if len(cuo_one) > 10:
            d_cd = len(cuo_one) - 10
            for i in xrange(d_cd):
                cuo_one.pop()
                cuo_two.pop()

    cuo_three_1 = tables.row_values(18)[4:14]
    cuo_fore_1 = tables.row_values(19)[4:14]
    cuo_three = []
    cuo_fore = []
    if cuo_three_1[0] == ' ':
        for i in xrange(10):
            cuo_three.append(' ')
            cuo_fore.append(' ')
    else:
        cuo_three_dict = {}
        for i in xrange(10):
            if cuo_fore_1[i] != ' ':
                cuo_three_dict[cuo_three_1[i]] = cuo_fore_1[i]
        cuo_three_dict = sorted(cuo_three_dict.items(), key=lambda x: abs(x[1]), reverse=True)
        for i in cuo_three_dict:

            cuo_three.append(i[0])
            cuo_fore.append(i[1])

        if cuo_fore[0] == ' ':
            cuo_fore = []
        cuo_fore = zh_bf(cuo_fore)

        if len(cuo_three) < 10:
            q_cd = 10 - len(cuo_three)
            for i in xrange(q_cd):
                cuo_three.append(' ')
                cuo_fore.append(' ')
        if len(cuo_three) > 10:
            d_cd = len(cuo_three) - 10
            for i in xrange(d_cd):
                cuo_three.pop()
                cuo_fore.pop()

    cuo_five_1 = tables.row_values(21)[4:14]
    cuo_six_1 = tables.row_values(22)[4:14]

    cuo_five = []
    cuo_six = []
    if cuo_five_1[0] == ' ':
        for i in xrange(10):
            cuo_five.append(' ')
            cuo_six.append(' ')
    else:
        cuo_five_dict = {}
        for i in xrange(10):
            if cuo_six_1[i] != ' ':
                cuo_five_dict[cuo_five_1[i]] = cuo_six_1[i]
        cuo_five_dict = sorted(cuo_five_dict.items(), key=lambda x: abs(x[1]), reverse=True)

        for i in cuo_five_dict:
            a = sdm_zh(i[0])
            cuo_five.append(a)
            cuo_six.append(i[1])

        if cuo_six[0] == ' ':
            cuo_six = []
        cuo_six = zh_bf(cuo_six)

        if len(cuo_five) < 10:
            q_cd = 10 - len(cuo_five)
            for i in xrange(q_cd):
                cuo_five.append(' ')
                cuo_six.append(' ')
        if len(cuo_five) > 10:
            d_cd = len(cuo_five) - 10
            for i in xrange(d_cd):
                cuo_five.pop()
                cuo_six.pop()


    cuo_seven_1 = tables.row_values(24)[4:14]
    cuo_eight_1 = tables.row_values(25)[4:14]

    cuo_seven = []
    cuo_eight = []
    if cuo_seven_1[0] == ' ':
        for i in xrange(10):
            cuo_seven.append(' ')
            cuo_eight.append(' ')
    else:
        cuo_seven_dict = {}
        for i in xrange(10):
            if cuo_eight_1[i] != ' ':
                cuo_seven_dict[cuo_seven_1[i]] = cuo_eight_1[i]
        cuo_seven_dict = sorted(cuo_seven_dict.items(), key=lambda x: abs(x[1]), reverse=True)

        for i in cuo_seven_dict:
            a = sdm_zh(i[0])
            cuo_seven.append(a)
            cuo_eight.append(i[1])

        if cuo_eight[0] == ' ':
            cuo_eight = []
        cuo_eight = zh_bf(cuo_eight)

        if len(cuo_seven) < 10:
            q_cd = 10 - len(cuo_seven)
            for i in xrange(q_cd):
                cuo_seven.append(' ')
                cuo_eight.append(' ')
        if len(cuo_seven) > 10:
            d_cd = len(cuo_seven) - 10
            for i in xrange(d_cd):
                cuo_seven.pop()
                cuo_eight.pop()


    cuo_nine_1 = tables.row_values(27)[4:14]
    cuo_ten_1 = tables.row_values(28)[4:14]

    cuo_nine = []
    cuo_ten = []
    if cuo_nine_1[0] == ' ':
        for i in xrange(10):
            cuo_nine.append(' ')
            cuo_ten.append(' ')
    else:
        cuo_nine_dict = {}
        for i in xrange(10):
            if cuo_ten_1[i] != ' ':
                cuo_nine_dict[cuo_nine_1[i]] = cuo_ten_1[i]
        cuo_nine_dict = sorted(cuo_nine_dict.items(), key=lambda x: abs(x[1]), reverse=True)

        for i in cuo_nine_dict:
            cuo_nine.append(i[0])
            cuo_ten.append(i[1])

        if cuo_ten[0] == ' ':
            cuo_ten = []
        cuo_ten = zh_bf(cuo_ten)

        if len(cuo_nine) < 10:
            q_cd = 10 - len(cuo_nine)
            for i in xrange(q_cd):
                cuo_nine.append(' ')
                cuo_ten.append(' ')
        if len(cuo_nine) > 10:
            d_cd = len(cuo_nine) - 10
            for i in xrange(d_cd):
                cuo_nine.pop()
                cuo_ten.pop()

    cuo_shiyi_1 = tables.row_values(30)[4:14]
    cuo_shier_1 = tables.row_values(31)[4:14]

    cuo_shiyi = []
    cuo_shier = []
    if cuo_shiyi_1[0] == ' ':
        for i in xrange(10):
            cuo_shiyi.append(' ')
            cuo_shier.append(' ')
    else:
        cuo_shiyi_dict = {}
        for i in xrange(10):
            if cuo_shier_1[i] != ' ':
                cuo_shiyi_dict[cuo_shiyi_1[i]] = cuo_shier_1[i]
        cuo_shiyi_dict = sorted(cuo_shiyi_dict.items(), key=lambda x: abs(x[1]), reverse=True)

        for i in cuo_shiyi_dict:
            cuo_shiyi.append(i[0])
            cuo_shier.append(i[1])

        if cuo_shier[0] == ' ':
            cuo_shier = []
        cuo_shier = zh_bf(cuo_shier)

        if len(cuo_shiyi) < 10:
            q_cd = 10 - len(cuo_shiyi)
            for i in xrange(q_cd):
                cuo_shiyi.append(' ')
                cuo_shier.append(' ')
        if len(cuo_shiyi) > 10:
            d_cd = len(cuo_shiyi) - 10
            for i in xrange(d_cd):
                cuo_shiyi.pop()
                cuo_shier.pop()


    # 处理有昨天为0前天不为0,或者前天为0，昨天不为0的数，展示到摘要页。

    sf_zero = []
    xf_zero = []
    cd_zero = []
    sfll_zero = []
    cdll_zero = []

    for i in xrange(2, 33):
        sf = table1.col_values(i)[:41]
        xf = table2.col_values(i)[:41]
        sfll = table4.col_values(i)[:41]

        # 注意格式，如果不是Int,下面判断==0就不成立，浮点数为0.0，然后注意sfxf[0]是省代码，要先摘出来。
        sf_sdm = sf[0]
        sf = zh_int(sf[1:])
        xf_sdm = xf[0]
        xf = zh_int(xf[1:])
        sfll_sdm = sfll[0]
        sfll = zh_int(sfll[1:])


        if (sf[38] == 0 and sf[39] != 0) or (sf[39] == 0 and sf[38] != 0):
            a = sdm_zh(sf_sdm)
            sf_zero.append(a)
        if (xf[38] == 0 and xf[39] != 0) or (xf[39] == 0 and xf[38] != 0):
            a = sdm_zh(xf_sdm)
            xf_zero.append(a)
        if (sfll[38] == 0 and sfll[39] != 0) or (sfll[39] == 0 and sfll[38] != 0):
            a = sdm_zh(sfll_sdm)
            sfll_zero.append(a)

    #错单也是浮点数，也需要转换成int
    for i in xrange(2, 13):
        cuod = table3.col_values(i)[:41]
        cdll = table5.col_values(i)[:41]
        cuod = zh_int(cuod[1:])
        cdll = zh_int(cdll[1:])

        if (cuod[38] == 0 and cuod[39] != 0) or (cuod[39] == 0 and cuod[38] != 0):
            cd_zero.append(cuod[0])
        if (cdll[38] == 0 and cdll[39] != 0) or (cdll[39] == 0 and cdll[38] != 0):
            cdll_zero.append(cdll[0])

    zd_zero = {}
    if len(sf_zero) != 0:
        zd_zero['sf'] = sf_zero
    else:
        zd_zero['sf'] = ''
    if len(xf_zero) != 0:
        zd_zero['xf'] = xf_zero
    else:
        zd_zero['xf'] = ''
    if len(cd_zero) != 0:
        zd_zero['cd'] = cd_zero
    else:
        zd_zero['cd'] = ''

    if len(sfll_zero) != 0:
        zd_zero['sfll'] = sfll_zero
    else:
        zd_zero['sfll'] = ''
    if len(cdll_zero) != 0:
        zd_zero['cdll'] = cdll_zero
    else:
        zd_zero['cdll'] = ''


    return render_mako_context(request, 'gprs/gprs_index.html', {'one': one,
                                                          'two': two,
                                                          'three': three,
                                                          'fore': fore,
                                                          'wu': wu,
                                                          'liu': liu,
                                                          'qi': qi,
                                                          'ba': ba,
                                                          'cuo_one': cuo_one,
                                                          'cuo_two': cuo_two,
                                                          'cuo_three': cuo_three,
                                                          'cuo_fore': cuo_fore,
                                                         'cuo_five':cuo_five,
                                                         'cuo_six':cuo_six,
                                                         'cuo_seven':cuo_seven,
                                                         'cuo_eight':cuo_eight,
                                                         'cuo_nine':cuo_nine,
                                                         'cuo_ten':cuo_ten,
                                                         'cuo_shiyi':cuo_shiyi,
                                                         'cuo_shier':cuo_shier,

                                                          'one_sum_1': one_sum_1,
                                                          'one_sum_10': one_sum_10,
                                                          'two_sum_1': two_sum_1,
                                                          'two_sum_10': two_sum_10,
                                                          'three_sum_1': three_sum_1,
                                                          'three_sum_10': three_sum_10,
                                                          'fore_sum_1':fore_sum_1,
                                                          'fore_sum_10':fore_sum_10,
                                                          'five_sum_1':five_sum_1,
                                                          'five_sum_10':five_sum_10,

                                                          'sf_zero': sf_zero,
                                                          'xf_zero': xf_zero,
                                                          'cd_zero': cd_zero,
                                                          'sfll_zero':sfll_zero,
                                                          'cdll_zero':cdll_zero,
                                                          'zd_zero': zd_zero,

                                                          })


#详细数据.将省代码传过来。
def xxsj(request,page,sdm):
    '''
    如果page是1,表示数据为上发，如果是2表示为下发，如果是3表示为错单。
    '''
    page = int(page)
    if page != 3:
        sdm = smc_zh(sdm)

    tables = gprs_data.sheets()[page]
    ri_q = tables.col_values(0)[1:41]

    # 查看摘要页是几天。这里取数据就取几天得值。
    tables = gprs_data.sheets()[0]
    two_tag = tables.row_values(5)[4]
    num = ''
    for i in two_tag:
        if i == ' ':
            continue
        if i.isdigit():
            num += i
        else:
            break
    num = int(num)
    z_num = 40 - num
    s_num = z_num - num

    z_ri_q = ri_q[z_num]
    s_ri_q = ri_q[s_num]



    #一共是31个省代码
    cd = 31
    if page == 3:
        #错单的是11个
        cd = 11
        send_type = '错单'
    if page == 1:
        send_type = '上发'
    if page == 2:
        send_type = '下发'


    tables = gprs_data.sheets()[page]
    #由于省代码是31个，由第二个开始就是1 到 33 ，所以省代码的列表就是下面的范围。2-32
    sdm_list = tables.row_values(0)[2:cd+2]

    for i in xrange(cd):
        if sdm_list[i] == sdm:
            i += 2
            info = tables.col_values(i)[1:41]

            infodr = foo(info[38], info[39])
            infotr = ten(info[20:30], info[30:40])
            #infor_t_pands = ten_pj_and_sum(info[20:30], info[30:40])
            infor_t_pands = ten_pj_and_sum(info[s_num:z_num], info[z_num:40])
            #前二十到前十的和
            q_ten_sum = infor_t_pands.get('0')[0]
            #前二十到前十的平均数
            q_ten_pj = infor_t_pands.get('0')[1]
            h_ten_sum = infor_t_pands.get('1')[0]
            h_ten_pj = infor_t_pands.get('1')[1]
            #这里一定要到最后转换成Int,否则计算的时候不能计算小数。整数相出得不到小数，xlrd读出来刚好是
            #浮点数，直接计算即可，完成后再转成int,这里是最近五天的数据。
            info = zh_int(info[-4:])
            #转成千分位
            info = qfw(info)

            sname = sdm
            if page != 3:
                #获取省代码对应省名称
                sname = sdm_zh(sdm)


    return render_mako_context(request, 'gprs/xxsj.html',{'info':info,
                                                           'infodr':infodr,
                                                           'infotr':infotr,
                                                           'q_ten_sum':q_ten_sum,
                                                           'q_ten_pj':q_ten_pj,
                                                           'h_ten_sum':h_ten_sum,
                                                           'h_ten_pj':h_ten_pj,
                                                           'send_type':send_type,
                                                           'sname':sname,
                                                          'ri_q':ri_q,
                                                          'z_ri_q':z_ri_q,
                                                          's_ri_q':s_ri_q,
                                                           })


def bo_d(request,name):

    #多了一个sum，直接把31改成32了。
    cd = 32
    bd = 16
    if name == 'cuod':
        # 错单的是11个,加上sum是12个
        cd = 12
        bd = 12
        page = 3
        send_type = '错单'
    if name == 'sf':
        send_type = '上发'
        page = 1
    if name == 'xf':
        page = 2
        send_type = '下发'
    if name == 'sfll':
        page = 4
        send_type = '上发流量'
    if name == 'cdll':
        page = 5
        cd = 12
        bd = 12
        send_type = '错误流量'


    tables = gprs_data.sheets()[page]
    # 由于省代码是31个，从第一个开始就是1到32，而下边的循环是从0开始，所以cd不能是32了。

    sdm_list = tables.row_values(0)[1:cd + 1]

    one_dr_list = []
    ten_tr_lsit = []
    #变色标志列表
    ten_bsbz = []
    one_bsbz = []


    for i in xrange(1,cd+1):
        #获取到第一个省代码开始的所有数据
        info = tables.col_values(i)[1:41]
        #计算出今天跟昨天的差值，然后返回出比例，添加到列表
        infodr = foo(info[38], info[39])
        one_dr_list.append(infodr)
        #计算出前二十天到前十天的差值比例，添加到列表.
        infotr = ten(info[20:30], info[30:40])
        ten_tr_lsit.append(infotr)
        #计算出差值，比例，但是不加百分比，用于比较大小，判断是否变色。
        ten_bz = ten_biao(info[20:30], info[30:40])
        ten_bsbz.append(ten_bz)
        one_bz = foo_bian(info[38],info[39])
        one_bsbz.append(one_bz)
    if name != 'cuod' and name != 'cdll':
        #如果不是错单，需要将省代码转换成名称.
        sdm_mingc = []
        for i in sdm_list:
            j = sdm_zh(i)
            if j == None:
                j = 'sum'
            sdm_mingc.append(j)
    else:
        sdm_mingc = sdm_list

    return render_mako_context(request,'gprs/bodong.html',{
        'one_dr_list':one_dr_list,
        'ten_tr_list':ten_tr_lsit,
        'sdm_mingc':sdm_mingc,
        'ten_bsbz':ten_bsbz,
        'one_bsbz':one_bsbz,
        'send_type':send_type,
        'cd':cd,
        'bd':bd,

    })



def xq(request):

    return render_mako_context(request,'gprs/xq.html')



#全量数据的展示。
def quanl(request,sdm,page):
    page = int(page)
    if page == 1:
        leix = '上发'
    if page == 2:
        leix = '下发'
    if page == 4:
        leix = '上发流量'

    # 定义省代码位于哪个区间
    a = ['北京','上海','重庆','广东','天津']
    b = ['辽宁','江苏','湖北','四川','陕西']
    c = ['河北','山西','河南','吉林','黑龙江']
    d = ['内蒙', '山东', '安徽', '浙江', '福建']
    e = ['湖南','广西','江西','贵州','云南']
    f = ['西藏','海南','甘肃','宁夏','青海','新疆']



    tables = gprs_data.sheets()[page]

    #设计的时候没有把sum加进去，这里加个判断，如果sdm是sum的话，说明前端页面点击的是sum
    if sdm == 'sum':
        #用于定位是第几个图.
        tu_num = 7
        #日期是固定的。
        ri_q = tables.col_values(0)[1:41]
        #sum列也是固定的
        info = tables.col_values(1)[1:41]

        #本来是要弄变色的，下面已经将变色的和百分比已经求出，但是之前已经弄过了，所以添加了个按钮，这个就不再作用了。
        infodr = foo(info[38], info[39])
        infodr_change = foo_bian(info[38], info[39])

        infotr = ten(info[20:30], info[30:40])
        infotr_change = ten_biao(info[20:30], info[30:40])

        s_mingc = 'sum'
        info = zh_int(info)
        info = qfw(info)

        return render_mako_context(request,'gprs/quanliang.html',{'sdm':s_mingc,
                                                           'ri_q':ri_q,
                                                           'info':info,
                                                           'infodr':infodr,
                                                           'infotr':infotr,
                                                           'leix':leix,
                                                            'infodr_change':infodr_change,
                                                           'infotr_change':infotr_change,
                                                               'page':page,
                                                               'tu_num':tu_num,
                                                           })



    # 由于省代码是31个，从第一个开始就是2到33，而下边的循环是从0开始。
    sdm_list = tables.row_values(0)[2: 33]
    for i in xrange(31):
        if sdm_list[i] == sdm:
            #由于再文件中第零个是别的数据，所以此时I要加2才是第一个省代码，北京。
            i += 2
            #日期列表，不包括deal_date
            ri_q = tables.col_values(0)[1:41]
            #数据列表
            info = tables.col_values(i)[1:41]
            #转为
            #一天
            infodr = foo(info[38], info[39])
            infodr_change = foo_bian(info[38], info[39])
            #十天
            infotr = ten(info[20:30], info[30:40])
            infotr_change = ten_biao(info[20:30], info[30:40])

            s_mingc = sdm_zh(sdm)
            if s_mingc in a:
                tu_num = 1
            if s_mingc in b:
                tu_num = 2
            if s_mingc in c:
                tu_num = 3
            if s_mingc in d:
                tu_num = 4
            if s_mingc in e:
                tu_num = 5
            if s_mingc in f:
                tu_num = 6

            info = zh_int(info)
            info = qfw(info)

            break


    return render_mako_context(request,'gprs/quanliang.html',{'sdm':s_mingc,
                                                           'ri_q':ri_q,
                                                           'info':info,
                                                           'infodr':infodr,
                                                           'infotr':infotr,
                                                           'leix':leix,
                                                            'infodr_change':infodr_change,
                                                           'infotr_change':infotr_change,
                                                            'page':page,
                                                           'tu_num':tu_num,
                                                           })

#错单全量的展示
def cuoql(request,page):

    leix = '错误全量'
    page = int(page)
    if page == 5:
        leix = '错误流量'
    tables = gprs_data.sheets()[page]
    zd_data = {}
    for i in xrange(41):
        a = tables.row_values(i)
        if i > 0:
            b = a[0]
            a = zh_int(a[1:])
            a = qfw(a)
            a.insert(0,b)
        zd_data[i] = a
    return render_mako_context(request,'gprs/cuoql.html',{'zd_data':zd_data,
                                                          'leix':leix,

                                                     })

#图形展示
def txzs(request,page):
    page = int(page)
    if page == 1:
        leix = '上发图形展示'
    if page == 2:
        leix = '下发图形展示'
    if page == 4:
        leix = '上发流量图形展示'
    if page == 3 or page == 5:
        leix = '错单图形展示'
        #用于鉴别是错单还是错误流量
        id_d = 3
        if page == 5:
            leix = '错误流量图形展示'
            id_d = 5

        tables = gprs_data.sheets()[page]
        # 第一行，省代码名称
        sdm = tables.row_values(0)[1:]
        # 第一列,日期，包含第一个deal_date
        d_date = tables.col_values(0)

        # 以下变量为了方便，懒得改名字了，与那些省代码无关。
        # F009
        beij = tables.col_values(2)[1:41]
        bjdr = foo(beij[38], beij[39])
        bjtr = ten(beij[20:30], beij[30:40])
        beij = zh_int(beij)

        # F050 以下均同上
        guangd = tables.col_values(3)[1:41]
        gddr = foo(guangd[38], guangd[39])
        gdtr = ten(guangd[20:30], guangd[30:40])
        guangd = zh_int(guangd)

        # F051
        shangh = tables.col_values(4)[1:41]
        shdr = foo(shangh[38], shangh[39])
        shtr = ten(shangh[20:30], shangh[30:40])
        shangh = zh_int(shangh)

        # F060
        tianj = tables.col_values(5)[1:41]
        tjdr = foo(tianj[38], tianj[39])
        tjtr = ten(tianj[20:30], tianj[30:40])
        tianj = zh_int(tianj)

        # F061
        chongq = tables.col_values(6)[1:41]
        cqdr = foo(chongq[38], chongq[39])
        cqtr = ten(chongq[20:30], chongq[30:40])
        chongq = zh_int(chongq)

        # F111
        liaon = tables.col_values(7)[1:41]
        lndr = foo(liaon[38], liaon[39])
        lntr = ten(liaon[20:30], liaon[30:40])
        liaon = zh_int(liaon)

        # F120
        jiangs = tables.col_values(8)[1:41]
        jsdr = foo(jiangs[38], jiangs[39])
        jstr = ten(jiangs[20:30], jiangs[30:40])
        jiangs = zh_int(jiangs)

        # F121
        hub = tables.col_values(9)[1:41]
        hbdr = foo(hub[38], hub[39])
        hbtr = ten(hub[20:30], hub[30:40])
        hub = zh_int(hub)

        # F122
        sic = tables.col_values(10)[1:41]
        scdr = foo(sic[38], sic[39])
        sctr = ten(sic[20:30], sic[30:40])
        sic = zh_int(sic)

        # F070
        shanxx = tables.col_values(11)[1:41]
        sxxdr = foo(shanxx[38], shanxx[39])
        sxxtr = ten(shanxx[20:30], shanxx[30:40])
        shanxx = zh_int(shanxx)

        # F020
        F020 = tables.col_values(12)[1:41]
        F020 = zh_int(F020)


        cuo_sum = tables.col_values(1)[1:41]
        cuo_sum = zh_int(cuo_sum)


        return render_mako_context(request, 'gprs/error.html', dictionary={'sdm': sdm,
                                                                                        'd_date': d_date,
                                                                                        'beij': beij,
                                                                                        'bjdr': bjdr,
                                                                                        'bjtr': bjtr,
                                                                                        'guangd': guangd,
                                                                                        'gddr': gddr,
                                                                                        'gdtr': gdtr,
                                                                                        'shangh': shangh,
                                                                                        'shdr': shdr,
                                                                                        'shtr': shtr,
                                                                                        'tianj': tianj,
                                                                                        'tjdr': tjdr,
                                                                                        'tjtr': tjtr,
                                                                                        'chongq': chongq,
                                                                                        'cqdr': cqdr,
                                                                                        'cqtr': cqtr,
                                                                                        'liaon': liaon,
                                                                                        'lndr': lndr,
                                                                                        'lntr': lntr,
                                                                                        'jiangs': jiangs,
                                                                                        'jsdr': jsdr,
                                                                                        'jstr': jstr,
                                                                                        'hub': hub,
                                                                                        'hbdr': hbdr,
                                                                                        'hbtr': hbtr,
                                                                                        'sic': sic,
                                                                                        'scdr': scdr,
                                                                                        'sctr': sctr,
                                                                                        'shanxx': shanxx,
                                                                                        'sxxdr': sxxdr,
                                                                                        'sxxtr': sxxtr,
                                                                                        'F020': F020,

                                                                                        'leix':leix,
                                                                                        'cuo_sum':cuo_sum,
                                                                                        'id_d':id_d,


                                                                                        })
    #此时的drtr已经没用了，以后有时间再优化。

    tables = gprs_data.sheets()[page]

    # 第一行，省代码名称
    sdm = tables.row_values(0)[1:]

    # 第一列,日期，包含第一个deal_date
    d_date = tables.col_values(0)

    # A_100 beij不包含，OneD_Rate   TenD_Rate，第二局调函数算出
    #这里是从2开始读数据，并没有将sum 放进去，因为sum 的值太大，放进去会影响看其他值得波动，所以把sum单拉出来。
    beij = tables.col_values(2)[1:41]
    bjdr = foo(beij[38], beij[39])
    bjtr = ten(beij[20:30], beij[30:40])
    beij = zh_int(beij)

    # A_200 以下均同上
    guangd = tables.col_values(3)[1:41]
    gddr = foo(guangd[38], guangd[39])
    gdtr = ten(guangd[20:30], guangd[30:40])
    guangd = zh_int(guangd)

    # A210
    shangh = tables.col_values(4)[1:41]
    shdr = foo(shangh[38], shangh[39])
    shtr = ten(shangh[20:30], shangh[30:40])
    shangh = zh_int(shangh)

    # A220
    tianj = tables.col_values(5)[1:41]
    tjdr = foo(tianj[38], tianj[39])
    tjtr = ten(tianj[20:30], tianj[30:40])
    tianj = zh_int(tianj)

    # A230
    chongq = tables.col_values(6)[1:41]
    cqdr = foo(chongq[38], chongq[39])
    cqtr = ten(chongq[20:30], chongq[30:40])
    chongq = zh_int(chongq)

    # A240
    liaon = tables.col_values(7)[1:41]
    lndr = foo(liaon[38], liaon[39])
    lntr = ten(liaon[20:30], liaon[30:40])
    liaon = zh_int(liaon)

    # A250
    jiangs = tables.col_values(8)[1:41]
    jsdr = foo(jiangs[38], jiangs[39])
    jstr = ten(jiangs[20:30], jiangs[30:40])
    jiangs = zh_int(jiangs)

    # A270
    hub = tables.col_values(9)[1:41]
    hbdr = foo(hub[38], hub[39])
    hbtr = ten(hub[20:30], hub[30:40])
    hub = zh_int(hub)

    # A280
    sic = tables.col_values(10)[1:41]
    scdr = foo(sic[38], sic[39])
    sctr = ten(sic[20:30], sic[30:40])
    sic = zh_int(sic)

    # A290 陕西，shanxx
    shanxx = tables.col_values(11)[1:41]
    sxxdr = foo(shanxx[38], shanxx[39])
    sxxtr = ten(shanxx[20:30], shanxx[30:40])
    shanxx = zh_int(shanxx)

    # A311 河北
    heb = tables.col_values(12)[1:41]
    hebdr = foo(heb[38], heb[39])
    hebtr = ten(heb[20:30], heb[30:40])
    heb = zh_int(heb)

    # A351 山西
    shanx = tables.col_values(13)[1:41]
    sxdr = foo(shanx[38], shanx[39])
    sxtr = ten(shanx[20:30], shanx[30:40])
    shanx = zh_int(shanx)

    # A371 河南
    hen = tables.col_values(14)[1:41]
    hendr = foo(hen[38], hen[39])
    hentr = ten(hen[20:30], hen[30:40])
    hen = zh_int(hen)

    # A431 吉林
    jil = tables.col_values(15)[1:41]
    jldr = foo(jil[38], jil[39])
    jltr = ten(jil[20:30], jil[30:40])
    jil = zh_int(jil)

    # A451 黑龙江
    heilj = tables.col_values(16)[1:41]
    hljdr = foo(heilj[38], heilj[39])
    hljtr = ten(heilj[20:30], heilj[30:40])
    heilj = zh_int(heilj)

    # A471 内蒙古
    neimg = tables.col_values(17)[1:41]
    nmgdr = foo(neimg[38], neimg[39])
    nmgtr = ten(neimg[20:30], neimg[30:40])
    neimg = zh_int(neimg)

    # A531 山东
    shand = tables.col_values(18)[1:41]
    sddr = foo(shand[38], shand[39])
    sdtr = ten(shand[20:30], shand[30:40])
    shand = zh_int(shand)

    # A551 安徽
    anh = tables.col_values(19)[1:41]
    ahdr = foo(anh[38], anh[39])
    ahtr = ten(anh[20:30], anh[30:40])
    anh = zh_int(anh)

    # A571 浙江
    zhej = tables.col_values(20)[1:41]
    zjdr = foo(zhej[38], zhej[39])
    zjtr = ten(zhej[20:30], zhej[30:40])
    zhej = zh_int(zhej)

    # A591 福建
    fuj = tables.col_values(21)[1:41]
    fjdr = foo(fuj[38], fuj[39])
    fjtr = ten(fuj[20:30], fuj[30:40])
    fuj = zh_int(fuj)

    # 731 湖南
    hun = tables.col_values(22)[1:41]
    hundr = foo(hun[38], hun[39])
    huntr = ten(hun[20:30], hun[30:40])
    hun = zh_int(hun)

    # A771 广西
    guangx = tables.col_values(23)[1:41]
    gxdr = foo(guangx[38], guangx[39])
    gxtr = ten(guangx[20:30], guangx[30:40])
    guangx = zh_int(guangx)

    # A791 江西
    jiangx = tables.col_values(24)[1:41]
    jxdr = foo(jiangx[38], jiangx[39])
    jxtr = ten(jiangx[20:30], jiangx[30:40])
    jiangx = zh_int(jiangx)

    # A851 贵州
    guiz = tables.col_values(25)[1:41]
    gzdr = foo(guiz[38], guiz[39])
    gztr = ten(guiz[20:30], guiz[30:40])
    guiz = zh_int(guiz)

    # A871 云南
    yunn = tables.col_values(26)[1:41]
    yndr = foo(yunn[38], yunn[39])
    yntr = ten(yunn[20:30], yunn[30:40])
    yunn = zh_int(yunn)

    # A891 西藏
    xiz = tables.col_values(27)[1:41]
    xzdr = foo(xiz[38], xiz[39])
    xztr = ten(xiz[20:30], xiz[30:40])
    xiz = zh_int(xiz)

    # A898 海南
    hain = tables.col_values(28)[1:41]
    hndr = foo(hain[38], hain[39])
    hntr = ten(hain[20:30], hain[30:40])
    hain = zh_int(hain)

    # A931 甘肃
    gans = tables.col_values(29)[1:41]
    gsdr = foo(gans[38], gans[39])
    gstr = ten(gans[20:30], gans[30:40])
    gans = zh_int(gans)

    # A951 宁夏
    ningx = tables.col_values(30)[1:41]
    nxdr = foo(ningx[38], ningx[39])
    nxtr = ten(ningx[20:30], ningx[30:40])
    ningx = zh_int(ningx)

    # A971 青海
    qingh = tables.col_values(31)[1:41]
    qhdr = foo(qingh[38], qingh[39])
    qhtr = ten(qingh[20:30], qingh[30:40])
    qingh = zh_int(qingh)

    # A991 新疆
    xinj = tables.col_values(32)[1:41]
    xjdr = foo(xinj[38], xinj[39])
    xjtr = ten(xinj[20:30], xinj[30:40])
    xinj = zh_int(xinj)

    #这个是sum列得图形展示
    beij_sum = tables.col_values(1)[1:41]
    beij_sum = zh_int(beij_sum)


    return render_mako_context(request, 'gprs/txzs.html', dictionary={'sdm': sdm,
                                                                                      'd_date': d_date,
                                                                                      'beij': beij,
                                                                                      'bjdr': bjdr,
                                                                                      'bjtr': bjtr,
                                                                                      'guangd': guangd,
                                                                                      'gddr': gddr,
                                                                                      'gdtr': gdtr,
                                                                                      'shangh': shangh,
                                                                                      'shdr': shdr,
                                                                                      'shtr': shtr,
                                                                                      'tianj': tianj,
                                                                                      'tjdr': tjdr,
                                                                                      'tjtr': tjtr,
                                                                                      'chongq': chongq,
                                                                                      'cqdr': cqdr,
                                                                                      'cqtr': cqtr,
                                                                                      'liaon': liaon,
                                                                                      'lndr': lndr,
                                                                                      'lntr': lntr,
                                                                                      'jiangs': jiangs,
                                                                                      'jsdr': jsdr,
                                                                                      'jstr': jstr,
                                                                                      'hub': hub,
                                                                                      'hbdr': hbdr,
                                                                                      'hbtr': hbtr,
                                                                                      'sic': sic,
                                                                                      'scdr': scdr,
                                                                                      'sctr': sctr,
                                                                                      'shanxx': shanxx,
                                                                                      'sxxdr': sxxdr,
                                                                                      'sxxtr': sxxtr,
                                                                                      'heb': heb,
                                                                                      'hebdr': hebdr,
                                                                                      'hebtr': hebtr,
                                                                                      'shanx': shanx,
                                                                                      'sxdr': sxdr,
                                                                                      'sxtr': sxtr,
                                                                                      'hen': hen,
                                                                                      'hendr': hendr,
                                                                                      'hentr': hentr,
                                                                                      'jil': jil,
                                                                                      'jldr': jldr,
                                                                                      'jltr': jltr,
                                                                                      'heilj': heilj,
                                                                                      'hljdr': hljdr,
                                                                                      'hljtr': hljtr,
                                                                                      'neimg': neimg,
                                                                                      'nmgdr': nmgdr,
                                                                                      'nmgtr': nmgtr,
                                                                                      'shand': shand,
                                                                                      'sddr': sddr,
                                                                                      'sdtr': sdtr,
                                                                                      'anh': anh,
                                                                                      'ahdr': ahdr,
                                                                                      'ahtr': ahtr,
                                                                                      'zhej': zhej,
                                                                                      'zjdr': zjdr,
                                                                                      'zjtr': zjtr,
                                                                                      'fuj': fuj,
                                                                                      'fjdr': fjdr,
                                                                                      'fjtr': fjtr,
                                                                                      'hun': hun,
                                                                                      'hundr': hundr,
                                                                                      'huntr': huntr,
                                                                                      'guangx': guangx,
                                                                                      'gxdr': gxdr,
                                                                                      'gxtr': gxtr,
                                                                                      'jiangx': jiangx,
                                                                                      'jxdr': jxdr,
                                                                                      'jxtr': jxtr,
                                                                                      'guiz': guiz,
                                                                                      'gzdr': gzdr,
                                                                                      'gztr': gztr,
                                                                                      'yunn': yunn,
                                                                                      'yndr': yndr,
                                                                                      'yntr': yntr,
                                                                                      'xiz': xiz,
                                                                                      'xzdr': xzdr,
                                                                                      'xztr': xztr,
                                                                                      'hain': hain,
                                                                                      'hndr': hndr,
                                                                                      'hntr': hntr,
                                                                                      'gans': gans,
                                                                                      'gsdr': gsdr,
                                                                                      'gstr': gstr,
                                                                                      'ningx': ningx,
                                                                                      'nxdr': nxdr,
                                                                                      'nxtr': nxtr,
                                                                                      'qingh': qingh,
                                                                                      'qhdr': qhdr,
                                                                                      'qhtr': qhtr,
                                                                                      'xinj': xinj,
                                                                                      'xjdr': xjdr,
                                                                                      'xjtr': xjtr,
                                                                      'beij_sum':beij_sum,
                                                                                      'page': page,
                                                                                    'leix':leix,

                                                                                      })


def dtxzs(request,page,number):

    page = int(page)
    number = int(number)
    leix = '错单图形展示'

    if page == 1:
        yema = 1
        leix = '上发图形展示'
    if page == 2:
        yema = 2
        leix = '下发图形展示'
    if page == 4:
        yema = 4
        leix = '上发流量图形展示'

    tables = gprs_data.sheets()[yema]

    # 第一行，省代码名称
    sdm = tables.row_values(0)[2:]

    # 第一列,日期，包含第一个deal_date
    d_date = tables.col_values(0)
    #定义一个保存原始省代码的列表，用于跳转到相应的全量
    ys_sdm = []
    if number == 1:
        lie_one = 2
        lie_two = 3
        lie_three = 4
        lie_fore = 5
        lie_five = 6

        sheng_mingc = []
        for i in sdm[:5]:
            j = sdm_zh(i)
            if j == None:
                j = 'sum'
            sheng_mingc.append(j)
            ys_sdm.append(i)

    if number == 2:
        lie_one = 7
        lie_two = 8
        lie_three = 9
        lie_fore = 10
        lie_five = 11
        sheng_mingc = []
        for i in sdm[5:10]:
            j = sdm_zh(i)
            sheng_mingc.append(j)
            ys_sdm.append(i)

    if number == 3:
        lie_one = 12
        lie_two = 13
        lie_three = 14
        lie_fore = 15
        lie_five = 16
        sheng_mingc = []
        for i in sdm[10:15]:
            j = sdm_zh(i)
            sheng_mingc.append(j)
            ys_sdm.append(i)
    if number == 4:
        lie_one = 17
        lie_two = 18
        lie_three = 19
        lie_fore = 20
        lie_five = 21
        sheng_mingc = []
        for i in sdm[15:20]:
            j = sdm_zh(i)
            sheng_mingc.append(j)
            ys_sdm.append(i)

    if number == 5:
        lie_one = 22
        lie_two = 23
        lie_three = 24
        lie_fore = 25
        lie_five = 26
        sheng_mingc = []
        for i in sdm[20:25]:
            j = sdm_zh(i)
            sheng_mingc.append(j)
            ys_sdm.append(i)
    if number == 6:
        lie_one = 27
        lie_two = 28
        lie_three = 29
        lie_fore = 30
        lie_five = 31
        lie_six = 32
        sheng_mingc = []
        for i in sdm[25:31]:
            j = sdm_zh(i)
            sheng_mingc.append(j)
            ys_sdm.append(i)





    if number == 6:

        # 如果是六的话说明是第六个，多一个.六个或者一个的使用的是错单的页面，但不一定是错单。
        # A_100 beij不包含，OneD_Rate   TenD_Rate，第二局调函数算出
        beij = tables.col_values(lie_one)[1:41]
        bjdr = foo(beij[38], beij[39])
        bjtr = ten(beij[20:30], beij[30:40])
        beij = zh_int(beij)


        # A_200 以下均同上
        guangd = tables.col_values(lie_two)[1:41]
        gddr = foo(guangd[38], guangd[39])
        gdtr = ten(guangd[20:30], guangd[30:40])
        guangd = zh_int(guangd)

        # A210
        shangh = tables.col_values(lie_three)[1:41]
        shdr = foo(shangh[38], shangh[39])
        shtr = ten(shangh[20:30], shangh[30:40])
        shangh = zh_int(shangh)

        # A220
        tianj = tables.col_values(lie_fore)[1:41]
        tjdr = foo(tianj[38], tianj[39])
        tjtr = ten(tianj[20:30], tianj[30:40])
        tianj = zh_int(tianj)

        # A230
        chongq = tables.col_values(lie_five)[1:41]
        cqdr = foo(chongq[38], chongq[39])
        cqtr = ten(chongq[20:30], chongq[30:40])
        chongq = zh_int(chongq)

        # A240
        liaon = tables.col_values(lie_six)[1:41]
        lndr = foo(liaon[38], liaon[39])
        lntr = ten(liaon[20:30], liaon[30:40])
        liaon = zh_int(liaon)

        return render_mako_context(request, 'gprs/cuodtxzs.html', {'d_date': d_date,
                                                                 'sdm': sheng_mingc,
                                                                   'ys_sdm':ys_sdm,
                                                                 'beij': beij,
                                                                 'bjdr': bjdr,
                                                                 'bjtr': bjtr,
                                                                 'guangd': guangd,
                                                                 'gddr': gddr,
                                                                 'gdtr': gdtr,
                                                                 'shangh': shangh,
                                                                 'shdr': shdr,
                                                                 'shtr': shtr,
                                                                 'tianj': tianj,
                                                                 'tjdr': tjdr,
                                                                 'tjtr': tjtr,
                                                                 'chongq': chongq,
                                                                 'cqdr': cqdr,
                                                                 'cqtr': cqtr,
                                                                 'liaon': liaon,
                                                                 'lndr': lndr,
                                                                 'lntr': lntr,
                                                                'leix':leix,
                                                                   'page':page,
                                                                 })

    if number == 7:
        lie_one = 1
        sheng_mingc = ['sum']
        beij_sum = tables.col_values(lie_one)[1:41]
        beij_sum = zh_int(beij_sum)


        return render_mako_context(request, 'gprs/dtxzs.html', {'d_date': d_date,
                                                               'sdm': sheng_mingc,
                                                               'beij': beij_sum,
                                                                   'leix':leix,
                                                                   'number':number,
                                                                'page':page,
                                                                   })


    # A_100 beij不包含，OneD_Rate   TenD_Rate，第二局调函数算出
    beij = tables.col_values(lie_one)[1:41]
    bjdr = foo(beij[38], beij[39])
    bjtr = ten(beij[20:30], beij[30:40])
    beij = zh_int(beij)


    # A_200 以下均同上
    guangd = tables.col_values(lie_two)[1:41]
    gddr = foo(guangd[38], guangd[39])
    gdtr = ten(guangd[20:30], guangd[30:40])
    guangd = zh_int(guangd)

    # A210
    shangh = tables.col_values(lie_three)[1:41]
    shdr = foo(shangh[38], shangh[39])
    shtr = ten(shangh[20:30], shangh[30:40])
    shangh = zh_int(shangh)

    # A220
    tianj = tables.col_values(lie_fore)[1:41]
    tjdr = foo(tianj[38], tianj[39])
    tjtr = ten(tianj[20:30], tianj[30:40])
    tianj = zh_int(tianj)

    # A230
    chongq = tables.col_values(lie_five)[1:41]
    cqdr = foo(chongq[38], chongq[39])
    cqtr = ten(chongq[20:30], chongq[30:40])
    chongq = zh_int(chongq)

    return render_mako_context(request,'gprs/dtxzs.html',{
                                                              'sdm':sheng_mingc,
                                                            'ys_sdm': ys_sdm,
                                                              'd_date': d_date,
                                                              'beij': beij,
                                                              'bjdr': bjdr,
                                                              'bjtr': bjtr,
                                                              'guangd': guangd,
                                                              'gddr': gddr,
                                                              'gdtr': gdtr,
                                                              'shangh': shangh,
                                                              'shdr': shdr,
                                                              'shtr': shtr,
                                                              'tianj': tianj,
                                                              'tjdr': tjdr,
                                                              'tjtr': tjtr,
                                                              'chongq': chongq,
                                                              'cqdr': cqdr,
                                                              'cqtr': cqtr,
                                                                'leix':leix,
                                                            'page':page,
                                                                    })


#此函数为错单得三个图形页面。上边那个是上下发图形展示得，六个图的，使用的这个页面。前端判断，如果是3，就是点击的三个图，也就是错单的sum
#上面的=6,就是第六个图，也是就三十一省的最后六个省。
def cuodtxzs(request,id_d,number):

    leix = '错单图形展示'
    number = int(number)
    id_d = int(id_d)
    yema = id_d
    if id_d == 5:
        yema = 5

    tables = gprs_data.sheets()[yema]

    # 第一行，省代码名称
    sdm = tables.row_values(0)[1:]
    # 第一列,日期，包含第一个deal_date
    d_date = tables.col_values(0)

    if number == 1:
        lie_one = 2
        lie_two = 3
        lie_three = 4
        lie_fore = 5
        lie_five = 6
        lie_six = 7
        sdm = sdm[1:7]

    if number == 2:
        lie_one = 8
        lie_two = 9
        lie_three = 10
        lie_fore = 11
        lie_five = 12
        sdm = sdm[7:12]

        # 以下变量为了方便，懒得改名字了，与那些省代码无关。
        # F009
        beij = tables.col_values(lie_one)[1:41]
        beij = zh_int(beij)

        # F050 以下均同上
        guangd = tables.col_values(lie_two)[1:41]
        guangd = zh_int(guangd)

        # F051
        shangh = tables.col_values(lie_three)[1:41]
        shangh = zh_int(shangh)

        # F060
        tianj = tables.col_values(lie_fore)[1:41]
        tianj = zh_int(tianj)

        # F061
        chongq = tables.col_values(lie_five)[1:41]
        chongq = zh_int(chongq)


        return render_mako_context(request, 'gprs/cuodtxzs.html', dictionary={'sdm': sdm,
                                                                              'd_date': d_date,
                                                                              'beij': beij,
                                                                              'guangd': guangd,
                                                                              'shangh': shangh,
                                                                              'tianj': tianj,
                                                                              'chongq': chongq,
                                                                              'number': number,
                                                                              'leix': leix,
                                                                              })

    if number == 3:
        lie_one = 1
        sdm = [sdm[0]]

        beij = tables.col_values(lie_one)[1:41]
        beij = zh_int(beij)

        return render_mako_context(request,'gprs/cuodtxzs.html',{'number':number,
                                                                         'sdm':sdm,
                                                                         'beij':beij,
                                                                         'd_date':d_date,
                                                                 'leix':leix,
                                        })

    # 以下变量为了方便，懒得改名字了，与那些省代码无关。
    # F009
    beij = tables.col_values(lie_one)[1:41]
    beij = zh_int(beij)

    # F050 以下均同上
    guangd = tables.col_values(lie_two)[1:41]
    guangd = zh_int(guangd)

    # F051
    shangh = tables.col_values(lie_three)[1:41]
    shangh = zh_int(shangh)

    # F060
    tianj = tables.col_values(lie_fore)[1:41]
    tianj = zh_int(tianj)

    # F061
    chongq = tables.col_values(lie_five)[1:41]
    chongq = zh_int(chongq)

    # F111
    liaon = tables.col_values(lie_six)[1:41]
    liaon = zh_int(liaon)



    return render_mako_context(request, 'gprs/cuodtxzs.html', dictionary={'sdm': sdm,
                                                                                    'd_date': d_date,
                                                                                    'beij': beij,
                                                                                    'guangd': guangd,
                                                                                    'shangh': shangh,
                                                                                    'tianj': tianj,
                                                                                    'chongq': chongq,
                                                                                    'liaon': liaon,
                                                                                    'number':number,
                                                                          'leix':leix,

                                                                                    })
