import unittest
import requests
import json

class MyTestCase(unittest.TestCase):
    def test_invitation1(self):
        file_object = open('session.txt', 'r')
        try:
            text = file_object.read()
        finally:
            file_object.close()
            print text
        params = {'invitation_id': 278}
        headers = {'Conten-Type': 'application/json;charset=UTF-8', 'cookie':text}
        url = "http://testapi.kitty.live/v1/account/share_user"
        r = requests.get(url, params=params, headers=headers)
        print "****result****"
        print r
        res = json.loads(r.content)
        print res
        print (r.status_code,type(r.status_code))
        self.assertEqual(r.status_code,200)
        self.assertIsInstance(res,dict)
        print res.keys()
        exceptkeys = {u'message',u'code',u'user'}
        self.assertEqual(sorted(res.keys()),sorted(exceptkeys))
        for values in res.values():
            print values
            self.assertNotEqual(values,u"")
        print "done  test1!!!!"
        #self.assertEqual(True, False)

    def test_invitation2(self):
        with open('session.txt','r') as f:
            text = (f.read())
        headers = {'Conten-Type': 'application/json;charset=UTF-8', 'cookie': text}
        url = "http://testapi.kitty.live/v1/account/share_user"
        r = requests.get(url,headers=headers)
        print "****result****"
        print (r.status_code, type(r.status_code))
        self.assertEquals(r.status_code, 200)
        res = json.loads(r.content)
        print res.keys
        values = '12001'
        for values in res.values():
            print values
        print "done  test2!!!!"

    def test_invitation3(self):
        with open('session.txt','r') as f:
            text = (f.read())
        params = {'invitation_id': '2.0'}
        headers = {'Conten-Type': 'application/json;charset=UTF-8', 'cookie': text}
        url = "http://testapi.kitty.live/v1/account/share_user"
        r = requests.get(url, params=params, headers=headers)
        print "****result****"
        print (r.status_code, type(r.status_code))
        self.assertNotEqual(r.status_code, 200)
        print "done test3!!!!"

    def test_invitation4(self):
        with open('session.txt','r') as f:
            text = (f.read())
        params = {'invitation_id': 'd'}
        headers = {'Conten-Type': 'application/json;charset=UTF-8',  'cookie': text}
        url = "http://testapi.kitty.live/v1/account/share_user"
        r = requests.get(url, params=params, headers=headers)
        print "****result****"
        print (r.status_code, type(r.status_code))
        self.assertNotEqual(r.status_code, 200)
        print "done test4!!!!"

if __name__ == '__main__':
    unittest.main()
