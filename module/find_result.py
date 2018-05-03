# -*- coding:utf-8 -*-
import re
from bs4 import BeautifulSoup

def find_result(result):
    soup = BeautifulSoup(result,"lxml")
    result = soup.findAll("p",{"class":"fontWeight lineHeight24"})
    if(result):
        result_sub = re.sub(u"\\<.*?\\>", "", str(result[0]))
    else:
        result_sub = "订单号有误啊亲"
    return result_sub