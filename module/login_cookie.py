# -*- coding:utf-8 -*-
from util import load_phantomjs
import time

def login_cookie(phantomjs,login_url,search_url):
    try:

        user_ID = input("请输入账号")
        user_Pwd = input("密码")

        phantomjs.get(login_url)
        


        time.sleep(3)


        phantomjs.find_element_by_id('merchantId').clear()
        phantomjs.find_element_by_id('merchantId').send_keys(user_ID)

        phantomjs.find_element_by_id('merchantPwd').clear()
        phantomjs.find_element_by_id('merchantPwd').send_keys(user_Pwd)

        phantomjs.find_element_by_id('merchantSafetyCodeBtn').click()
        time.sleep(3)
        SafetyCode = input("请输入随机码")
        phantomjs.find_element_by_id('merchantSafetyCode').clear()
        phantomjs.find_element_by_id('merchantSafetyCode').send_keys(SafetyCode)

        phantomjs.find_element_by_id('merchantLogin').click()

        time.sleep(3)

   
        phantomjs_cookie = phantomjs.get_cookies()

    finally:
    	phantomjs.close()
    return phantomjs_cookie