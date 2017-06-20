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

        url = "http://testapi.kitty.live/v1/user/invitor?device_id=123456789"
        headers = {'Conten-Type': 'application/json;charset=UTF-8', 'cookie':text}

        r = requests.get(url=url,headers=headers)
        print r
        print (r.status_code,type(r.status_code))
        self.assertEqual(r.status_code,200)
        print "*****done*****"


if __name__ == '__main__':
    unittest.main()
