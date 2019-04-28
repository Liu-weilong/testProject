#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/4/15 16:09
#@Author: liuweilong
#@File  : desired_caps.py
from appium import webdriver
import logging
import yaml
import os

#生成日志信息
logging.basicConfig(filename='../logs/run.log',level=logging.DEBUG,datefmt='%Y-%m-%d %H:%M:%S',format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
#logging.basicConfig(filename='run.log',level=logging.DEBUG,format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')


def appium_descap():
    # file = open('../config/kyb_caps.yaml','r')
    # data = yaml.load(file)
    with open('../config/kyb_caps.yaml','r',encoding='utf-8') as file:
        data = yaml.load(file)

    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platforVersion'] = data['platforVersion']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['udid'] = data['udid']
    # base_dir = os.path.dirname(os.path.dirname(__file__))
    # app_path = os.path.join(base_dir,'app',data['appname'])
    desired_caps['app'] = data['app']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['noReset'] = data['noReset']
    desired_caps['ip'] = data['ip']
    desired_caps['port'] = data['port']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']
    #dirver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
    dirver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    dirver.implicitly_wait(10)
    return dirver
#testProject/app/kaoyanbang_3.3.6.242.apk  /storage/emulated/0/Apps/20190416155217303.apk
if __name__ == '__main__':
    # with open('../config/kyb_caps.yaml','r',encoding='utf-8') as file:
    #     data = yaml.load(file)
    #     base_dir = os.path.dirname(os.path.dirname(__file__))
    #     app_path = os.path.join(base_dir, 'app', data['app'])
    #     print(data)
    appium_descap()
















