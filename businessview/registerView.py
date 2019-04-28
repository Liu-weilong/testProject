#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/4/25 15:12
#@Author: liuweilong
#@File  : registerView.py
import logging,random
from testProject.common.desired_caps import appium_descap
from testProject.common.common_fun import Common,By,NoSuchElementException

class RegisterView(Common):

    reg_text = (By.ID,'注册页面的id')
    reg_head = (By.ID,'头像元素')
    reg_heads = (By.ID,'图片')
    reg_baocun = (By.ID,'保存')

    reg_name = (By.ID,'用户名')
    reg_pwd = (By.ID,'密码')
    reg_eml = (By.ID,'邮箱')

    reg_sumit = (By.ID,'立即注册')

    def register_action(self,reg_name,reg_pwd,reg_eml):
        self.check_cancelBtn()
        self.dirver.find_element(*self.reg_text).click()
        self.dirver.find_element(*self.reg_head).click()
        self.dirver.find_elements(*self.reg_heads)[5].click()
        self.dirver.find_element(*self.reg_baocun).click()

        self.find_element(*self.reg_name).send_keys('')
        self.find_element(*self.reg_pwd).send_keys('')
        self.find_element(*self.reg_eml).send_keys('')
        self.find_element(*self.reg_sumit).click()


if __name__ == '__main__':
    dirver = appium_descap()
    po = RegisterView(dirver)
    po.register_action('','','')
    po.check_loginStatus()



