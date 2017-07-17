# -*- coding:utf-8 -*-
import  requests
import  json
import  unittest
from kittylive_test.utils import common_check
###直播分类列表             writer  xiaoyuer
####  country字段为空或者错误时，，都可以请求成功，所以这块目前没做处理
class MyTestCase(unittest.TestCase):

    def setUp(self):
        file_cookle = open("D:\cookles.txt", 'r')
        self.cookles_session = file_cookle.read()
        file_cookle.close()
        self.headers = {'Conten-Type': 'application/json;charset=UTF-8', 'cookie': 'session=' + self.cookles_session}
        self.url="http://testapi.kitty.live/v1/live/category"

    def test_liveclassification_1(self):
        print  "直播模块_直播分类"
        params = {'country': 'TH'}
        res = requests.get(url=self.url, params=params,headers=self.headers)
        exceptkeys = [u'category', u'message', u'total', u'code']
        res_dict=common_check.common_check(self,res)
        common_check.common_check_dict(self,res_dict,exceptkeys,True)
        print "=======test_live_classification test1 done======="


    def test_liveclassification_2(self):
        print  "直播模块_直播分类"
        params = {'country': ''}
        res = requests.get(url=self.url, params=params, headers=self.headers)
        common_check.common_check(self, res)
        print "=======test_live_classification test2 done======="

    def test_liveclassification_3(self):
        print  "直播模块_直播分类"
        params = {'country': '1245'}
        res = requests.get(url=self.url, params=params, headers=self.headers)
        common_check.common_check(self, res)
        print "=======test_live_classification test2 done======="


if __name__ == '__main__':
    unittest.main()


