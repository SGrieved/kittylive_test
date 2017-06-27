import unittest
import json
import sys
import requests

class UserRecommand(unittest.TestCase):

    def test_userrecommand(self):
        file_object = open('session.txt','r')
        with open('session.txt','r') as f:
            text = (f.read())
        params = {'page':1,'size':20}
        headers = {'Conten-Type':'application/json;charset=UTF-8','cookie':text}
        url = "http://testapi.kitty.live/v1/recommand/hot"
        r = requests.get(url,params=params,headers=headers)
        print r
        res = json.loads(r.content)
        print res
        print(r.status_code,type(r.status_code))
        self.assertEqual(r.status_code,200)
        self.assertIsInstance(res,dict)
        print res.keys()
        exceptkeys = [u'show_pos',u'message',u'code',u'recommand_list']
        self.assertEqual(sorted(res.keys()),sorted(exceptkeys))
        for values in res.values():
            print (values)
            self.assertNotEqual(values,u"")
        print "done"

if __name__ == '__main__':
    unittest.main()
