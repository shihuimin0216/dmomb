# !/usr/bin/env python
# coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
import urllib, sys
import ssl
# -*- coding: utf-8 -*-
import random

def generate_verification_code(len):
     # ''' 随机生成6位的验证码 '''
     # 注意： 这里我们生成的是0-9A-Za-z的列表，当然你也可以指定这个list，这里很灵活
     # 比如： code_list = ['P','y','t','h','o','n','T','a','b'] # PythonTab的字母
    code_list = []
    for i in range(10): # 0-9数字
        code_list.append(str(i))
    for i in range(65, 91): # 对应从“A”到“Z”的ASCII码
        code_list.append(chr(i))
    for i in range(97, 123): #对应从“a”到“z”的ASCII码
        code_list.append(chr(i))
    myslice = random.sample(code_list, len) # 从list中随机获取6个元素，作为一个片断返回
    verification_code = ''.join(myslice) # list to string
    return verification_code
def sendSms(phone):
    # python3示例代码下载链接
    # http://code.fegine.com/python3Demo.zip

    host = 'https://feginesms.market.alicloudapi.com'
    path = '/codeNotice'
    method = 'POST'
    appcode = 'af17a518790e4711b578fd77a5fb22a9'
    verification_code =''.join(generate_verification_code(len=6))
    print(type(verification_code))
    print("verification_code",verification_code)
    querys = 'param='+verification_code+'&phone='+phone+'&sign=500451&skin=900652'
    bodys = {}
    url = host + path + '?' + querys
    request = urllib.request.Request(url)
    request.add_header('Authorization', 'APPCODE ' + appcode)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    response = urllib.request.urlopen(request, context=ctx)
    content = response.read()
    if (content):
        print(content)
    return verification_code
    ######################
    # client = AcsClient('LTAI4Fp71Nyzhsb5XiDy9Aiy', 'O6b8TDn8pH23x62nk6tjaNuYDsmgpc', 'cn-hangzhou')
    # request = CommonRequest()
    # request.set_accept_format('json')
    # request.set_domain('dysmsapi.aliyuncs.com')
    # request.set_method('POST')
    # request.set_protocol_type('https')  # https | http
    # request.set_version('2017-05-25')
    # request.set_action_name('SendSms')
    #
    # request.add_query_param('RegionId', "cn-hangzhou")
    # request.add_query_param('PhoneNumbers', "15162780073")
    # request.add_query_param('SignName', "sign=500451")
    # request.add_query_param('TemplateCode', "skin=900652")
    # request.add_query_param('TemplateParam', "{\"code\":\"122111\"}")
    #
    # response = client.do_action(request)
    # # python2:  print(response)
    # # print(str(response, encoding='utf-8'))
    # return str(response, encoding='utf-8')
