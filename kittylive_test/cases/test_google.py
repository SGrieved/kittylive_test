# -*- coding:utf-8 -*-
import unittest
import requests
import json
from kittylive_test.utils import common_check

class MyTestCase(unittest.TestCase):
    def test_google1(self):
        with open('session.txt','r') as f:
            text = (f.read())
        post_data = {'product_id':53,'payload':''}
        data = json.dumps(post_data)
        url = "http://testapi.kitty.live/v1/pay/google/create?platform=1&version_code=64"
        headers = {'Conten-Type': 'application/json;charset=UTF-8', 'cookie': text}
        r = requests.post(url=url,data=data,headers=headers)
        res_dict = common_check.common_check(self,r)
        exceptkeys = {u'message',u'code',u'transaction_id'}
        common_check.common_check_dict(self, res_dict, exceptkeys, True, [])
        print "google ok"

    def test_google2(self):
        with open('session.txt','r') as f:
            text = (f.read())
        #post_data = {}
        #data = json.dumps(post_data)
        url = "http://testapi.kitty.live/v1/pay/google/create?platform=1&version_code=64"
        headers = {'Conten-Type': 'application/json;charset=UTF-8', 'cookie': text}
        r = requests.post(url=url,headers=headers)
        print r
        self.assertNotEqual(r.status_code,200)
        print "no data"

    def test_google3(self):
        with open('session.txt','r') as f:
            text = (f.read())
        post_data = {'product_id':'53','payload':''}
        data = json.dumps(post_data)
        url = "http://testapi.kitty.live/v1/pay/google/create?platform=1&version_code=64"
        headers = {'Conten-Type': 'application/json;charset=UTF-8', 'cookie': text}
        r = requests.post(url=url,data=data,headers=headers)
        res_dict = common_check.common_check(self,r)
        exceptkeys = {u'message',u'code'}
        common_check.common_check_dict(self, res_dict, exceptkeys, True, [])
        print "product not found 4005"

    def test_google4(self):
        with open('session.txt','r') as f:
            text = (f.read())
        post_data = {'product_id':10,'payload':''}
        data = json.dumps(post_data)
        url = "http://testapi.kitty.live/v1/pay/google/create?platform=1&version_code=64"
        headers = {'Conten-Type': 'application/json;charset=UTF-8', 'cookie': text}
        r = requests.post(url=url,data=data,headers=headers)
        res_dict = common_check.common_check(self,r)
        exceptkeys = {u'message',u'code'}
        common_check.common_check_dict(self, res_dict, exceptkeys, True, [])
        print "product not available"

    def test_google5(self):
        with open('session.txt','r') as f:
            text = (f.read())
        post_data = {'product_id':59,'payload':''}
        data = json.dumps(post_data)
        url = "http://testapi.kitty.live/v1/pay/google/create?platform=1&version_code=64"
        headers = {'Conten-Type': 'application/json;charset=UTF-8', 'cookie': text}
        r = requests.post(url=url,data=data,headers=headers)
        res_dict = common_check.common_check(self,r)
        exceptkeys = {u'message',u'code'}
        common_check.common_check_dict(self, res_dict, exceptkeys, True, [])
        print "recharge limit"

if __name__ == '__main__':
    unittest.main()


