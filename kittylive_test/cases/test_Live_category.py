# -*- coding:utf-8 -*-
import  requests
import  json
import  unittest

class MyTestCase(unittest.TestCase):
    def setUp(self):
        with open('session.txt', 'r') as f:
            text = (f.read())
        self.headers = {'Conten-Type': 'application/json;charset=UTF-8', 'cookie': text}
        self.url="http://testapi.kitty.live/v1/live/category"

    def test_liveclassification_1(self):
        print  "直播模块_直播分类"
        params = {'country': 'TH'}
        res = requests.get(url=self.url, params=params,headers=self.headers)
        back_json = json.loads(res.content)
        print back_json
        print (res.status_code, type(res.status_code))
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(back_json, dict)
        print (back_json.keys())
        exceptkeys = [u'category', u'message', u'total', u'code']
        self.assertEqual(sorted(back_json.keys()), sorted(exceptkeys))
        # for value in back_json.values():
        #     self.assertNotEqual(value, u"")
        #     print value
        print "=======test_live_classification test1 done======="


    def test_liveclassification_2(self):
        print  "直播模块_直播分类"
        params = {'country': ''}
        res = requests.get(url=self.url, params=params, headers=self.headers)
        print (res.status_code, type(res.status_code))
        self.assertEqual(res.status_code, 200)
        print "=======test_live_classification test2 done======="

    def test_liveclassification_3(self):
        print  "直播模块_直播分类"
        params = {'country': '1245'}
        res = requests.get(url=self.url, params=params, headers=self.headers)
        print (res.status_code, type(res.status_code))
        self.assertEqual(res.status_code, 200)
        print "=======test_live_classification test2 done======="


if __name__ == '__main__':
    unittest.main()


