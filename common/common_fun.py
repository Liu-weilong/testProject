#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/4/16 10:55
#@Author: liuweilong
#@File  : common_fun.py
from testProject.baseView.baseView import BaseView
from testProject.common.desired_caps import appium_descap
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
import time,os
import csv

class Common(BaseView):

    # cancelBtn = (By.ID,'ID')
    # skipBtn = (By.ID,'ID')

    #进入app  点击2步 进入登录页面
    def check_cancelBtn(self):
        logging.info('come on')
        try:
            cancelBtn = self.dirver.find_element_by_id('com.fzisen.app51zxw:id/radiobutton_friend')
        except NoSuchElementException:
            print('no')
        else:
            cancelBtn.click()
            self.dirver.find_element_by_id('com.fzisen.app51zxw:id/tv_login').click()

    #获取屏幕尺寸
    def get_size(self):
        x = self.dirver.get_window_size()['wight']
        y = self.dirver.get_window_size()['height']
        return x,y

    def getTime(self):
        self.now = time.strftime('%Y-%m-%d %H-%M-%S')
        return self.now

    #截图方法
    def getScreenshot(self,module):
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s_%s.png' %(module,time)

        self.dirver.get_screenshot_as_file(image_file)

    #去除登陆成功  有广告悬浮的操作
    def check_market_ad(self):
        logging.info('ad xuanfu')
        try:
            element = self.dirver.find_element_by_id('悬浮广告的id值')
        except NoSuchElementException:
            pass
        else:
            element.click()

    #读取csv数据方法
    def get_csv_data(self,csv_file,line):
        with open(csv_file,'r',encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index,row in enumerate(reader,1):
                if index == line:
                    return row
    # csv_file = '../data/accout.csv'
    # data = get_csv_data(csv_file,1)
    # print(data)





# if __name__ == '__main__':
    # dirver = appium_descap()
    # com = Common(dirver)
    # com.getScreenshot('start')
    # list = ['测试','数据','信息','管理']
    # list1 = ['测试', '数据', '信息', '管理','刘伟龙','15256750385']
    # for i in list:
    #     print(i)
    #
    # for i in range(len(list)):
    #     print(i,list[i])
    #
    # for index,item in enumerate(list1):
    #     print(index,item)




