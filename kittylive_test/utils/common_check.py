# -*- coding: utf-8  -*-
#!/usr/local/bin/python

__version__ = "1.0"
__license__ = "Copyright (c) 2014-2020, levp-inc, All rights reserved."
__author__  = "lisong <lisong@letvpicture.com>"

import unittest
import requests
import json
import sys

def common_check(self, response,right_status=True):
    '''
    公共校验方法
    验证"message", "version", "timestamp"在返回的response中，如若不在，则错误
    :rtype : object
    '''

    # 校验http的状态码
    status_code = [200]

    #判断是否是json类型
    try:
        response_dict = json.loads(response.content)
    except:
        print "response is not json format",response.content
        sys.exit()

    if right_status:
       self.assertIn(response.status_code, status_code)
#          判断message,version,timestamp是否存在
#       if 'message' not in response_dict or 'version' not in response_dict or 'timestamp' not in response_dict:
#           self.assertFalse(True)
    else:
        self.assertNotEqual(response.status_code, status_code)
    print response.status_code

    # 校验是否只返回三个参数
#    default_keys = [u'message', u'version', u'timestamp']
#    res_keys=sorted(response_dict.keys())
#    except_keys=sorted(default_keys)
#    self.assertEqual(res_keys, except_keys)

    # 检验response_dict中返回的message,version,timestamp的values均在
#    self.assertNotEqual(response_dict['message'], u'')
#    self.assertNotEqual(response_dict['version'], u'')
#    self.assertNotEqual(response_dict['timestamp'], u'')

    # 校验message的值是否与预期一致
    # if response_dict['message'] == exceptvalues:
    #     return response_dict
    # else:
    #     print response_dict['message']
    #     self.assertFalse(True)


    return response_dict


def common_check_dict(self, back_dict, exceptkeys, reverse=True, remove_key=[],typedict={}):
    '''检查dict类型的,keys，values不为空'''
    self.assertIsInstance(back_dict, dict)
    '''dict中keys排序'''
    res_keys=sorted(back_dict.keys())
    except_keys=sorted(exceptkeys)
    self.assertEqual(res_keys, except_keys)

    if reverse:
        '''遍历值且检查值不为空'''
        for remove_keys in remove_key:
            del back_dict[remove_keys]
        for values in back_dict.values():
            self.assertNotEqual(values, u'')
    else:
        '''遍历值且检查值可以为空'''
        self.assertFalse(False)
    if typedict:
        for info in typedict.keys():
            self.assertIsInstance(back_dict[info], typedict[info])


def common_check_list(self, back_list, reverse=True):
    ''' 检查list类型的,values不为空，返回列表遍历后的值 '''
    self.assertIsInstance(back_list, list)
    '''遍历值且检查值不为空'''
    if reverse:
        for values in back_list:
            self.assertNotEqual(values, u'')

    else:
        for values in back_list:
            if values is '[]':
                return '[]'
            else:
                return values


