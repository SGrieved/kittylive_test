
__author__ = 'lisong'
from django.conf import settings
settings.configure()
import requests
import json
import unittest
from kittylive_test.utils import common_check

class login_check_version(unittest.TestCase):
    '''
    kittylive:
    check version
    '''
    def test_login_check_version(self):
        ''''''
        post_data = {'platform':'2','version_code':'9'}
        response = requests.get("http://testapi.kitty.live/version/checkupdate", params=post_data)
        res_dict = common_check.common_check(self,response)
        exceptkeys = [u'notify_start',u'code',u'force',u'url',u'version_code',u'notify_end',u'build',u'message',u'content',u'version_name']
        common_check.common_check_dict(self,res_dict,exceptkeys,True,[u'version_name'])
if __name__ == '__main__':
    unittest.main()