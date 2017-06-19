import requests
import json

def get_cookie():
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

    print ('; '.join(['='.join(item) for item in cookies.items()]))


if __name__ == "__main__":
    get_cookie()