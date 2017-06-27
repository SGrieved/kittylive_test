# -*- coding:utf-8 -*-
import unittest
import requests
import json

class MyTestCase(unittest.TestCase):
    def test_packet_send1(self):
        file_object = open('session.txt', 'r')
        try:
            text = file_object.read()
        finally:
            file_object.close()
            print text
        post_data = {'live_id':'1900564','room_id':'123456','total_ruby':'9','total_size':'3'}
        url = "http://testapi.kitty.live/v1/packet/send"
        headers = {'Conten-Type': 'application/json;charset=UTF-8', 'cookie': text}
        data = json.dumps(post_data)
        r = requests.post(url=url,data=data,headers=headers)
        print r
        res = json.loads(r.content)
        print res
        print (r.status_code,type(r.status_code))
        self.assertEqual(r.status_code,200)
        self.assertIsInstance(res,dict)
        print res.keys()
        exceptkeys = {u'message',u'code',u'packet'}
        self.assertEquals(sorted(res.keys()),sorted(exceptkeys))
        for values in res.values():
            self.assertNotEquals(values,u"")
            print values
        print "packet send done1"

    def test_packet_send2(self):
        file_object = open('session.txt', 'r')
        try:
            text = file_object.read()
        finally:
            file_object.close()
            print text
        post_data = {'room_id': '123456', 'total_ruby': '9', 'total_size': '3'}
        url = "http://testapi.kitty.live/v1/packet/send"
        headers = {'Conten-Type': 'application/json;charset=UTF-8', 'cookie': text}
        data = json.dumps(post_data)
        r = requests.post(url=url, data=data, headers=headers)
        print r
        res = json.loads(r.content)
        print res
        print (r.status_code, type(r.status_code))
        self.assertNotEquals(r.status_code, 200)
        print "packet send done2"

    def test_packet_send4(self):
        file_object = open('session.txt', 'r')
        try:
            text = file_object.read()
        finally:
            file_object.close()
            print text
        post_data = {'live_id':'123456','room_id':'123456','total_ruby':'9','total_size':'3'}
        url = "http://testapi.kitty.live/v1/packet/send"
        headers = {'Conten-Type': 'application/json;charset=UTF-8', 'cookie': text}
        data = json.dumps(post_data)
        r = requests.post(url=url,data=data,headers=headers)
        print r
        res = json.loads(r.content)
        print res
        print (r.status_code,type(r.status_code))
        self.assertEqual(r.status_code,200)
        self.assertIsInstance(res,dict)
        print res.keys()
        exceptkeys = {u'message',u'code'}
        self.assertEquals(sorted(res.keys()),sorted(exceptkeys))
        for values in res.values():
            self.assertNotEquals(values,u"")
            print values
        print "packet send done4 ----liveID not found"

if __name__ == '__main__':
    unittest.main()
