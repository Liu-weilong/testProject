#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/4/25 16:14
#@Author: liuweilong
#@File  : test_register.py
from testProject.common.myunit import StandEnd
from businessview.registerView import RegisterView
from testProject.common.common_fun import *
import logging,random,unittest2

class RegisterTest(StandEnd):

    def test_user_register(self):
        logging.info('test reg')
        r = RegisterView(self.dirver)
        self.assertTrue(r.register_action('liuweilong','1711365302@qq.com','123456789'))
        self.dirver.getScreenshot('successs')

if __name__ == '__main__':
    unittest2.main()
