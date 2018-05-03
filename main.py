# -*- coding:utf-8 -*-
from module import login_cookie
from util import load_phantomjs
import requests
import os
from module.cout import cout
from util.set_cookie import set_cookie

def do():
    phantomjs = load_phantomjs.load_phantomjs()

    url = "http:"#登陆的网页

    search_url = "http:"#查询的网页

    cookie_list = login_cookie.login_cookie(phantomjs,url,search_url)

    cookie = set_cookie(cookie_list)

    cout('AdminStaff='+cookie['AdminStaff'],search_url)

    return

if __name__ == '__main__' :
    do()