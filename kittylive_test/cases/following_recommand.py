import unittest
import requests
import json

class MyTestCase(unittest.TestCase):
    def test_following_recommand(self):
        params = {'page': 1, 'size': 20}
        headers = {'Conten-Type': 'application/json;charset=UTF-8', 'cookie': 'session=1051460.qc6vGzNXQf_aiCdW'}
        url = "http://testapi.kitty.live/v1/recommand/following"
        r = requests.get(url, params=params, headers=headers)
        print "****result****"
        print r
        res = json.loads(r.content)
        print "****json result****"
        print res
        print "****print response code****"
        print(r.status_code,type(r.status_code))
        self.assertEqual(r.status_code,200)
        print "200 ok done"
        self.assertIsInstance(res,dict)
        print "*****keys*****"
        print res.keys()
        exceptkeys = {u'message',u'code',u'recommand_list'}
        self.assertEqual(sorted(res.keys()),sorted(exceptkeys))
        for values in res.values():
            self.assertNotEqual(values,u"")
            print values
        print "done"

if __name__ == '__main__':
    unittest.main()
