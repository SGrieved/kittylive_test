#!/usr/bin/env python
# encoding: utf-8

__version__ = "1.0"
__license__ = "Copyright (c) 2014-2020, levp-inc, All rights reserved."
__author__  = "lisong <lisong@letvpicture.com>"

import random

from utils.sms import SmsClient
from libs.cache import REDIS_CONN
from conf.redis_key_conf import RedisKeyConf

CAPTCHA_KV_PREFIX = RedisKeyConf.CAPTCHA_KV_PREFIX

def mobile_captcha(mobile):
    captcha = generate_captcha(4)
    SmsClient().send_sms(mobile, u'您的手机校验码:%s'%(captcha))
    get_captcha = REDIS_CONN.get(CAPTCHA_KV_PREFIX + mobile)
    return get_captcha

def generate_captcha(count):
    items = random.sample('0123456789', count)
    result = "".join([i for i in items])
    return result

def verify_captcha(captcha_key, captcha_value):

    if not captcha_value:
        return False
    else:
        server_captcha = REDIS_CONN.get(CAPTCHA_KV_PREFIX + captcha_key)
        if server_captcha != captcha_value:
            return False

    REDIS_CONN.delete(captcha_key)
    return True
