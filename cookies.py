#第一段代码
#coding=utf-8
from selenium import webdriver
import time,os
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
#获取cookie信息
cookie = driver.get_cookies()
#将获取的cookies信息打印
print(cookie)
print('*'*100)
for cookie in driver.get_cookies():
   print("%s -> %s" %(cookie['name'],cookie['value']))
# driver.get("http://www.youdao.com")
# driver.add_cookie({'name': 'key-aaaaaaa','value': 'value-bbbbbb'})
# for cookie in driver.get_cookies():
#    print("%s -> %s" %(cookie['name'],cookie['value']))
time.sleep(3)
driver.quit()


#第二段代码
from selenium import webdriver
from time import *
driver = webdriver.Chrome()
driver.get("https://xxxxxxxxxx")
sleep(6)
# 添加Cookie
driver.add_cookie({'name':'xxxx','value':'xxxxxxxxxxx'})

# 刷新页面
driver.refresh()

#关闭浏览器
driver.quit()
