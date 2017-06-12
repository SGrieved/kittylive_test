__author__ = 'lisong'
import requests
import json
import sys
import unittest
from kittylive_test.utils import common_check
class upload(unittest.TestCase):
    def test_upload(self):
        post_data = {'S':'1031.dciahHUWk_zFePoR'}
        files = {'file': open("abc.zip", 'rb')}
        #response = requests.post(url, data=data, files=files)
        #request_headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:30.0) Gecko/20100101 Firefox/30.0"}
        response = requests.post("http://pspm.pingstart.com/campaign/upload", data=post_data , files=files )
        #res_dict = common_check(response)
        #print(res_dict)
        print response
        print response.content
        print "*****************"
        res = json.loads(response.content)
        print res
        print "*****************"
        # print(response.status_code,type(response.status_code))
        # self.assertEqual(response.status_code,200)
        # self.assertIsInstance(res,dict)
        # print "*****************"
        # print(res.keys())
        # exceptkeys = [u'notify_start',u'code',u'force',u'url',u'version_code',u'notify_end',u'build',u'message']
        # self.assertEqual(sorted(res.keys()),sorted(exceptkeys))
        # for values in res.values():
        #     self.assertNotEqual(values,u"")
#if __name__ == "__main__":
#     self=''
#     login_check_version(self)
#if __name__ == "__main__":
#     self=''
#     login_check_version(self)