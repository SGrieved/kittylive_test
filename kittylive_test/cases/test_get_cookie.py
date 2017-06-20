import unittest
import requests
import json

class MyTestCase(unittest.TestCase):
    def test_get_cookie(self):
        post_data = {'country_code':'86','phone':'18211136932','password':'111111'}
        data = json.dumps(post_data)
        session = requests.session()
        url = "http://testapi.kitty.live/v1/account/login"
        response = session.post(url,data=data)
        cookies = requests.utils.dict_from_cookiejar(session.cookies)
        res = requests.post(url=url,data=data)
        if u'ging' in res.text:
            print "login ok"
        else:
            print "login fail"

        ses = '; '.join(['='.join(item) for item in cookies.items()])
        print ses
        file_object = open('session.txt','w')
        file_object.write(ses)
        file_object.close()
        print "write done"


if __name__ == '__main__':
    unittest.main()
