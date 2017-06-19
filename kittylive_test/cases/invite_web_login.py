import unittest
import requests
import json

class MyTestCase(unittest.TestCase):
    def test_invite_web_login(self):
        post_data = {'openid':'120578321810268','username':'wangwang','platform':1,'invitation_id':18}
        url = "http://testapi.kitty.live/v1/account/web_login"
        #headers = {'Conten-Type': 'application/json;charset=UTF-8', 'cookie': 'session=1051460.qc6vGzNXQf_aiCdW'}
        data = json.dumps(post_data)
        r = requests.post(url,data=data)
        print r
        res = json.loads(r.content)
        print res
        print (r.status_code,type(r.status_code))
        self.assertEqual(r.status_code,200)
        self.assertIsInstance(res,dict)
        print res.keys()
        exceptkeys = {u'message',u'code',u'register'}
        self.assertEqual(sorted(res.keys()),sorted(exceptkeys))
        for values in res.values():
            self.assertNotEqual(values,u"")
            print values
        print "*****done*****"


        #self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
