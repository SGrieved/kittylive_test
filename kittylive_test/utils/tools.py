#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "1.0"
__license__ = "Copyright (c) 2014-2020, levp-inc, All rights reserved."
__author__  = "lisong <lisong@letvpicture.com>"

import os, sys
PROJ_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)),'../')
sys.path.append(PROJ_ROOT)

import os

# 本文件存放一些针对乐影的公共方法

def absolute_path():
    '''
    获取当前的文件路径
    '''
    path=os.path.dirname(__file__)
    path=path[0:-5]
    return path
