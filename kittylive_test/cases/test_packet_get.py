# -*- coding:utf-8 -*-
import unittest
import requests
import json

class MyTestCase(unittest.TestCase):
    def test_packet_get(self):
        with open('session.txt','r') as f:
            text = (f.read())
        post_data = {"packet_id":3504}
        data = json.dumps(post_data)
        url = "http://testapi.kitty.live/v1/packet/get"
        headers = {'Conten-Type': 'application/json;charset=UTF-8', 'cookie': text}
        r = requests.post(url=url,data=data,headers=headers)
        print r
        res = json.loads(r.content)
        print res
        print (r.status_code,type(r.status_code))
        self.assertEquals(r.status_code,200)
        self.assertIsInstance(res,dict)
        print res.keys()
        exceptkeys = {u'message',u'code',u'ruby'}
        keys1 = sorted(res.keys())
        keys2 = sorted(exceptkeys)
        if keys1 == keys2:
            print "got packet success"
        else:
            print "You already got the packet"


if __name__ == '__main__':
    unittest.main()
