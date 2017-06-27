# -*- coding:utf-8 -*-
import unittest
import requests
import json
from kittylive_test.utils import common_check

class MyTestCase(unittest.TestCase):
    def test_apple(self):
        with open('session.txt', 'r') as f:
            text = (f.read())
        post_data = {'product_id':65,'payload':''}
        data = json.dumps(post_data)
        url = "http://testapi.kitty.live/v1/pay/apple/create?platform=2&version_code=102"
        headers = {'Conten-Type': 'application/json;charset=UTF-8', 'cookie': text}
        r = requests.post(url=url,data=data,headers=headers)
        res_dict = common_check.common_check(self, r)
        exceptkeys = {u'message', u'code', u'transaction_id'}
        common_check.common_check_dict(self, res_dict, exceptkeys, True, [])
        print "apple ok"


if __name__ == '__main__':
    unittest.main()
