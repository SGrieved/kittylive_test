# -*- coding:utf-8 -*-
import  requests
import  json
import unittest
from kittylive_test.utils import common_check
###直播分类下的直播列表    writer xiaoyuer
class MyTestCase(unittest.TestCase):

    def setUp(self):
        file_cookle = open('session.txt', 'r')
        cookles_text = file_cookle.read()
        file_cookle.close()
        self.headers = {'Conten-Type': 'application/json;charset=UTF-8', 'cookie': cookles_text}
        self.url = "http://testapi.kitty.live/v1/live/category/livelist"

    def test_livelist_1(self):
            params = {'start': '5', 'size': '5', 'country': 'TH', 'category_id': 12}  ###这里的size和start值是随机填写的
            res = requests.get(url=self.url, params=params, headers=self.headers)
            exceptkeys = [u'total', u'message', u'code', u'lives']
            res_dict=common_check.common_check(self,res,True)
            common_check.common_check_dict(self,res_dict,exceptkeys,True)
            common_check.common_check_list(self,[],True)
            print "=======test_category_livelist test done======="
            print "test_1 done"

    def test_livelist_2(self):
            ##start为空
            params = {'start': '', 'size': '5', 'country': 'TH', 'category_id': 12}  ###这里的size和start值是随机填写的
            res = requests.get(url=self.url, params=params, headers=self.headers)
            # print (res.status_code, type(res.status_code))
            # self.assertNotEqual(res.status_code, 200)
            res_dict = common_check.common_check(self, res, True)
            print "test_2  done"

    def test_livelist_3(self):
            ###start 值错误
            params = {'start': '#4vxyth', 'size': '5', 'country': 'TH', 'category_id': 12}  ###这里的size和start值是随机填写的
            res = requests.get(url=self.url, params=params, headers=self.headers)
            res_dict = common_check.common_check(self, res, True)
            print "test_3 done"

    def test_livelist_4(self):
            ###size值为空
            params = {'start': '5', 'size': '', 'country': 'TH', 'category_id': 12}  ###这里的size和start值是随机填写的
            res = requests.get(url=self.url, params=params, headers=self.headers)
            res_dict = common_check.common_check(self, res, True)
            # print (res.status_code, type(res.status_code))
            # self.assertNotEqual(res.status_code, 200)
            print "test_4 done "

    def test_livelist_5(self):
            ###size值错误
            params = {'start': '5', 'size': '@#56', 'country': 'TH', 'category_id': 12}  ###这里的size和start值是随机填写的
            res = requests.get(url=self.url, params=params, headers=self.headers)
            res_dict = common_check.common_check(self, res, True)
            # print (res.status_code, type(res.status_code))
            # self.assertNotEqual(res.status_code, 200)
            print "test_5 done "

    def test_livelist_6(self):
            ###country 为空
            params = {'start': '5', 'size': '5', 'country': '', 'category_id': 12}  ###这里的size和start值是随机填写的
            res = requests.get(url=self.url, params=params, headers=self.headers)
            res_dict = common_check.common_check(self, res, True)
            # print (res.status_code, type(res.status_code))
            # # self.assertNotEqual(res.status_code, 200)
            print "test_6 done "

    def test_livelist_7(self):
            ###country 错误
            params = {'start': '5', 'size': '5', 'country': 'ww', 'category_id': 12}  ###这里的size和start值是随机填写的
            res = requests.get(url=self.url, params=params, headers=self.headers)
            res_dict = common_check.common_check(self, res, True)
            # print (res.status_code, type(res.status_code))
            # self.assertEquals(res.status_code,200)
            print "test_7 done "

    def test_livelist_8(self):
            ###category_id为空
            params = {'start': '5', 'size': '5', 'country': 'TH', 'category_id': ''}  ###这里的size和start值是随机填写的
            res = requests.get(url=self.url, params=params, headers=self.headers)
            res_dict = common_check.common_check(self, res, True)
            # print (res.status_code, type(res.status_code))
            # self.assertEquals(res.status_code, 200)
            # self.assertNotEqual(res.status_code, 200)
            print "test_8 done "

    def test_livelist_9(self):
            ###category_id错误
            params = {'start': '5', 'size': '5', 'country': 'TH', 'category_id': '#246'}  ###这里的size和start值是随机填写的
            res = requests.get(url=self.url, params=params, headers=self.headers)
            res_dict = common_check.common_check(self, res, True)
            # print (res.status_code, type(res.status_code))
            # self.assertEquals(res.status_code, 200)
            # self.assertNotEqual(res.status_code, 200)
            print "test_9 done "

if __name__ == '__main__':
    unittest.main()
