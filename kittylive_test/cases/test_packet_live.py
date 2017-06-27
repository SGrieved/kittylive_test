# -*- coding:utf-8 -*-
import unittest
import json
import requests
from kittylive_test.utils import common_check

class MyTestCase(unittest.TestCase):
    def test_packet_live(self):
        with open('session.txt','r') as f:
            text = (f.read())
        params = {'live_id':1900564}
        url = "http://testapi.kitty.live/v1/packet/live"
        headers = {'Conten-Type': 'application/json;charset=UTF-8', 'cookie': text}
        r = requests.get(url=url,params=params,headers=headers)
        print r
        res_dict = common_check.common_check(self, r)
        exceptkeys = {u'message',u'code',u'packet'}
        common_check.common_check_dict(self, res_dict, exceptkeys, True, [])
        print "*********ok********"


if __name__ == '__main__':
    unittest.main()
