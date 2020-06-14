

#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
client = AcsClient('LTAI4G24j5rNWCraZe8NDq3o', 'q0tO4HhyzZA18RVOZVCmH2jHZfdvWB', 'cn-hangzhou')

def send_sms(phone,code):
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')  # https | http
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_query_param('PhoneNumbers', phone)
    request.add_query_param('SignName', "小饭桌管理平台")
    request.add_query_param('TemplateCode', "SMS_146806055")
    request.add_query_param('TemplateParam', "{\"code\":\"%s\"}" % code)


    response = client.do_action(request)
    # python2:  print(response)
    print(str(response, encoding='utf-8'))
