#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/4/16 11:34
#@Author: liuweilong
#@File  : test_login.py
from testProject.common.desired_caps import appium_descap
from testProject.common.myunit import StandEnd
from testProject.businessview.loginView import LoginView
import unittest2
import logging
from testProject.common.common_fun import *

class Testlogin(StandEnd):
    csv_file = '../data/accout.csv'
    def test_login_zxw(self):
        l = LoginView(self.dirver)
        data = l.get_csv_data(self,csv_file,2)
        l.login_action(data[0],data[1])
        self.assertTrue(l.check_loginStatus())
        self.dirver.getScreenshot('test_success')

    def test_login_zxw1(self):
        l = LoginView(self.dirver)
        data = l.get_csv_data(self,csv_file,3)
        l.login_action(data[0],data[1])
        self.assertTrue(l.check_loginStatus())
        self.dirver.getScreenshot('log_zxw')


if __name__ == '__main__':
    unittest2.main()

