# -*- coding:utf-8 -*-
import requests
from util.file_readlines import file_readlines
from util.http_req import http_req
from module.find_result import find_result
from module.login_cookie import login_cookie
import os

def cout(cookie,search_url):

    s = requests.session()

    result_all = []

    find_Result = []

    all_r = []

    orderNo = file_readlines()
    for i in range(len(orderNo)):
        result_all.append(http_req(s,orderNo[i],cookie,search_url))
        find_Result.append(find_result(result_all[i]))
        all_r.append(orderNo[i] + "\t" +  find_Result[i])
        a = str(i+1)
        print("第"+a+"个，doing...")

    file = open(r'./结果.txt','w')
    for i in range(len(all_r)):
        file.write(all_r[i])
        file.write('\n')
    file.close()
    print("导出到 结果.txt")
    os.system("pause")
