# -*- coding:utf-8 -*-
#cookie from phantomjs to requests
def set_cookie(cookie_list):
    phantomjs_cookie = cookie_list
    requests_cookie = {}
    for i in range(len(phantomjs_cookie)):
        requests_cookie[phantomjs_cookie[i]['name']] = phantomjs_cookie[i]['value'] 
    return requests_cookie
