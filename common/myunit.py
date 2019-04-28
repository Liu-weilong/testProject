#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/4/16 11:30
#@Author: liuweilong
#@File  : myunit.py
import unittest2
from testProject.common.desired_caps import appium_descap
import logging
from time import sleep

class StandEnd(unittest2.TestCase):
    def setUp(self):
        self.dirver = appium_descap()

    def tearDown(self):
        self.dirver.close()