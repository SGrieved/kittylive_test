# -*- coding: utf-8  -*-
#!/usr/local/bin/python

__version__ = "1.0"
__license__ = "Copyright (c) 2014-2020, levp-inc, All rights reserved."
__author__  = "lisong <lisong@letvpicture.com>"

import requests

from rest_framework.test import APITestCase
from tests.utils.common_check import common_check


def gen_after_cookies(self):

    TK=None

    # 乐影登录获取tk的方法
    url = '/rest/1.0/leying/users/login/'
    params={'loginname': '13261585190', 'password': '123456'}
    # 验证token是否有值
    if TK:
	checkurl = '/rest/1.0/leying/users/token/%s/check/'
	responsec = self.clent.get(checkurl%TK)
	res_dict = common_check(self, responsec, 'Succeed', True)
	if res_dict['message'] == 'Succeed':
       	    print TK
	    return TK
    else:
	response = self.client.post(url, data=params, format='json')
        response_dict = common_check(self, response, 'Succeed', True)
	TK = response_dict['sso_tk']
        print response_dict
        return TK

# if __name__ == "__main__":
#     gen_after_cookies()
