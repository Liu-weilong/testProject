#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/4/23 10:25
#@Author: liuweilong
#@File  : run.py
import logging
import time
import unittest2
from BSTestRunner import BSTestRunner

test_dir = '../test_case'
test_pretect = '../reports'
discovery = unittest2.defaultTestLoader.discover(test_dir,pattern='test*.py')
#logging.basicConfig(filename='../logs/run.log',level=logging.DEBUG,datefmt='%Y-%m-%d %H:%M:%S',format='')
logging.basicConfig(filename='../logs/run.log',level=logging.DEBUG,datefmt='%Y-%m-%d %H:%M:%S',format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
now = time.strftime('%Y-%m-%d %H-%M-%S')
test_report = test_pretect + '/' + now + 'result.html'
with open(test_report,'wb') as f:
    runner = BSTestRunner(stream=f,title='APP report',description='Report the results')
    runner.run(discovery)
    f.close()

