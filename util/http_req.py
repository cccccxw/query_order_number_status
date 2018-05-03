# -*- coding:utf-8 -*-
import requests
def http_req(s,order_no,cookie,search_url):

    R_url = search_url

    R_data = {'orderNo':order_no,
            'pageSize':'5',
            'page.webPager.action':'refresh',
            'page.webPager.pageInfo.totalSize':'1000',
            'page.webPager.pageInfo.pageSize':'5',
            'page.webPager.currentPage':'1'
              }

    R_headers = {
                'Accept':'*/*',
                'Accept-Encoding':'gzip, deflate',
                'Accept-Language':'zh-CN,zh;q=0.8',
                'Content-Length':'158',
                'Content-Type':'application/x-www-form-urlencoded',
                'Host':'admin.mall.10010.com',
              # 'Origin':#商城主页网址
                'Proxy-Connection':'keep-alive',
                'Referer':search_url,
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
                'X-Requested-With':'XMLHttpRequest',
                }
    R_headers['Cookie'] = cookie
    result = s.post(R_url,data = R_data,headers = R_headers).text
    return result