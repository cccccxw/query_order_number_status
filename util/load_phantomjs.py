# -*- coding:utf-8 -*-
from selenium import webdriver


def load_phantomjs():
    phantomjs = webdriver.PhantomJS(executable_path=r'.\phantomjs.exe')
    phantomjs.set_window_size(20,20)
    return phantomjs
