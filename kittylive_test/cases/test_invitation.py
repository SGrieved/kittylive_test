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
        params = {'invitation_id': ''}
        headers = {'Conten-Type': 'application/json;charset=UTF-8', 'cookie': 'session=1051460.qc6vGzNXQf_aiCdW'}
        url = "http://testapi.kitty.live/v1/account/share_user"
        r = requests.get(url,params=params,headers=headers)
        print "****result****"
        print (r.status_code, type(r.status_code))
        self.assertNotEqual(r.status_code, 200)
        print "done  test2!!!!"

    def test_invitation3(self):
        params = {'invitation_id': '2.0'}
        headers = {'Conten-Type': 'application/json;charset=UTF-8', 'cookie': 'session=1051460.qc6vGzNXQf_aiCdW'}
        url = "http://testapi.kitty.live/v1/account/share_user"
        r = requests.get(url, params=params, headers=headers)
        print "****result****"
        print (r.status_code, type(r.status_code))
        self.assertNotEqual(r.status_code, 200)
        print "done test3!!!!"

    def test_invitation4(self):
        params = {'invitation_id': 'd'}
        headers = {'Conten-Type': 'application/json;charset=UTF-8', 'cookie': 'session=1051460.qc6vGzNXQf_aiCdW'}
        url = "http://testapi.kitty.live/v1/account/share_user"
        r = requests.get(url, params=params, headers=headers)
        print "****result****"
        print (r.status_code, type(r.status_code))
        self.assertNotEqual(r.status_code, 200)
        print "done test4!!!!"

if __name__ == '__main__':
    unittest.main()
