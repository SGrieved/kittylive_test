__author__ = 'lisong'
#from django.conf import settings
#settings.configure()
import requests
import json
from rest_framework.test import APITestCase
import sys
import unittest
#from kittylive_test.utils import common_check


#class CheckVersionCase(APITestCase):
#    '''
#    kittyLive
#    update:check version
#    '''

#    def setUp(self):




class login_check_version_2(unittest.TestCase):


    def test_o22(self):
        b=3
        self.assertEqual(b,3)

if __name__ == '__main__':
    unittest.main()