#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/4/16 11:10
#@Author: liuweilong
#@File  : loginView.py
import logging
from testProject.common.common_fun import Common,NoSuchElementException
from testProject.common.desired_caps import appium_descap
from selenium.webdriver.common.by import By
#from PageObject.Baseview.baseview import BaseView
#from selenium.common.exceptions import NoSuchElementException
import unittest2


class LoginView(Common):

    #这是根据 我要自学网app进行的测试
    username_type = (By.ID,'com.fzisen.app51zxw:id/ed_username')
    password_type = (By.ID,'com.fzisen.app51zxw:id/ed_pass')
    loginbtn = (By.ID,'com.fzisen.app51zxw:id/tv_login')


    #登录状态检查元素
    usercenter = (By.ID,'com.fzisen.app51zxw:id/radiobutton_friend')
    #vbmoney = (By.LINK_TEXT,'liuweilong1992,您好')#LINK_TEXT
    mygb = (By.ID,'com.fzisen.app51zxw:id/bt_personal_attention')
    mygb_kc = (By.LINK_TEXT,'Python入门教程')

    #退出登录com.fzisen.app51zxw:id/bt_personal_attention
    logout_set = (By.ID,'com.fzisen.app51zxw:id/bt_account_set')
    logout_zx = (By.ID,'com.fzisen.app51zxw:id/tv_logout')
    cancel_out = (By.ID,'com.fzisen.app51zxw:id/btn_pos')


    #登录com.fzisen.app51zxw:id/tv_login
    def login_action(self,username,password):
        self.check_cancelBtn()
        logging.info('login in')
        self.dirver.find_element(*self.username_type).send_keys(username)
        self.dirver.find_element(*self.password_type).send_keys(password)
        self.dirver.find_element(*self.loginbtn).click()


    #检查登录状态 是否成功
    def check_loginStatus(self):
        self.check_cancelBtn()
        logging.info('check in status')
        #self.assertEqual(mygb_kc,'Python入门教程')
        try:
            self.dirver.find_element(*self.usercenter).click()
            self.dirver.find_element(*self.mygb).click()
            self.dirver.find_element(*self.mygb_kc)
        except NoSuchElementException:
            logging.info('login fail')
            self.getScreenshot('login_fail')
            return False
        else:
            logging.info('login success')
            self.exit_action()
            return True

    #退出登录
    def exit_action(self):
        logging.info('logout action')
        self.dirver.find_element(*self.logout_set).click()
        self.dirver.find_element(*self.logout_zx).click()
        self.dirver.find_element(*self.cancel_out).click()


if __name__ == '__main__':
        dirver = appium_descap()
        l = LoginView(dirver)
        l.login_action('1711365301@qq.com','lwl0909///')
        l.check_loginStatus()
        #l.exit_action()



