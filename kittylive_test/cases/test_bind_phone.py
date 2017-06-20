import unittest
import requests
import json

class MyTestCase(unittest.TestCase):
    def test_sms_send(self):
        file_object = open('session.txt', 'r')
        try:
            text = file_object.read()
        finally:
            file_object.close()
            print text

        post_data = {'country_code':'86','phone':'18211136932','sms_token':'c75d36a8-4859-46fd-b98d-2d635d953b7c','sms_code':'801012'}
        url = "http://testapi.kitty.live/v1/account/bind_mobile"
        headers = {'Conten-Type': 'application/json;charset=UTF-8', 'cookie':text}
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
        self.assertEqual(sorted(res.keys()),sorted(exceptkeys))
        for values in res.values():
            self.assertNotEqual(values,u"")
            print values

        print "*****done*****"



if __name__ == '__main__':
    unittest.main()
