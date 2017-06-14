__author__ = 'lisong'
import requests
import json
import sys
import unittest
from kittylive_test.utils import common_check
class login_check_version(unittest.TestCase):
    def test_login_check_version(self):
        post_data = {'platform':'2','version_code':'9'}
        #request_headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:30.0) Gecko/20100101 Firefox/30.0"}
        response = requests.get("http://testapi.kitty.live/version/checkupdate", params=post_data)
        #res_dict = common_check(response)
        #print(res_dict)
        print response
        print "*****************"
        res = json.loads(response.content)
        print res
        print "*****************"
        print(response.status_code,type(response.status_code))
        self.assertEqual(response.status_code,200)
        self.assertIsInstance(res,dict)
        print "*****************"
        print(res.keys())
        exceptkeys = [u'notify_start',u'code',u'force',u'url',u'version_code',u'notify_end',u'build',u'message',u'content',u'version_name']
        self.assertEqual(sorted(res.keys()),sorted(exceptkeys))
        del res[u'version_name']
        print res.keys()
        for values in res.values():
            print(values)
            self.assertNotEqual(values,u"")
#if __name__ == "__main__":
#     self=''
#     login_check_version(self)
#if __name__ == "__main__":
#     self=''
#     login_check_version(self)