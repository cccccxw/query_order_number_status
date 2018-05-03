# -*- coding:utf-8 -*-
def file_readlines():
    file = open(r'./订单号码.txt','r').readlines()    
    for i in range(len(file)):
        if file[i][-1]=='\n':
            file[i]=file[i][:-1]

    return file
