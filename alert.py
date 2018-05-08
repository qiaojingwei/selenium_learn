#Alert(driver).accept()  # 等同于点击“确认”或“OK”
#Alert(driver).dismiss()  # 等同于点击“取消”或“Cancel”
#Alert(driver).authenticate(username,password)  # 验证，针对需要身份验证的alert，目前还没有找到特别合适的示例页面
#Alert(driver).send_keys(keysToSend)  # 发送文本，对有提交需求的prompt框（上图3）
#Alert(driver).text  # 获取alert文本内容，对有信息显示的alert框

#示例1：switch_to.alert , accept() , text,测试链接http://sahitest.com/demo/alertTest.htm
# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('http://sahitest.com/demo/alertTest.htm')

driver.find_element_by_name('b1').click()

a1 = driver.switch_to.alert  # 通过switch_to.alert切换到alert
sleep(1)
print a1.text  # text属性输出alert的文本
a1.accept()  # alert“确认”
sleep(1)

driver.quit()
#运行结果:Alert Message


#示例2：Alert(driver) , dismiss(),测试链接http://sahitest.com/demo/confirmTest.htm
# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.alert import Alert

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('http://sahitest.com/demo/confirmTest.htm')

driver.find_element_by_name('b1').click()

a1 = Alert(driver)  # 直接实例化Alert对象
sleep(1)
print a1.text  # text属性输出alert的文本
a1.dismiss()  # alert“取消”
sleep(1)

driver.quit()
#运行结果:Some question?


#示例3：switch_to.alert , send_keys(keysToSend),测试链接http://sahitest.com/demo/promptTest.htm
# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('http://sahitest.com/demo/promptTest.htm')

driver.find_element_by_name('b1').click()

a1 = driver.switch_to.alert  # 通过switch_to.alert切换到alert
sleep(1)
print a1.text  # text属性输出alert的文本
a1.send_keys('send some words to alert!')  # 往prompt型alert中传入字符串
sleep(1)
a1.accept()
print driver.find_element_by_name('t1').get_attribute('value')
driver.quit()
#运行结果：
#Some prompt?
#send some words to alert!
