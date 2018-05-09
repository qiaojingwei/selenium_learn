#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,os

class Login():
	def __init__(self,driver,url,account_list,loged_url):
		self.driver = driver
		self.login_url = url
		self.account_list = account_list
		self.loged_url = loged_url
	def openUrl(self):
		self.driver.get(self.login_url)
	def get_web_ele(self):
		# time.sleep(2)
		WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.LINK_TEXT,'登录'))) #注意括号
    
		login_btn = self.driver.find_element_by_link_text('登录')
		usr_ele = self.driver.find_element_by_id('id_account_l')
		pwd_ele = self.driver.find_element_by_id('id_password_l')
		login_ok = self.driver.find_element_by_id('login_btn')
		# time.sleep(2)
		return login_btn,usr_ele,pwd_ele,login_ok
	def login_opre(self):
		self.openUrl()
		for account in self.account_list:
			ele_tuple = self.get_web_ele()
			ele_tuple[0].click()
			try:
				ele_tuple[1].send_keys(account['usrname'])
				ele_tuple[2].send_keys(account['pwd'])
				ele_tuple[3].click()
				time.sleep(2)
				if driver.current_url == self.loged_url:
					print('登录成功')
					self.driver.find_element_by_class_name('sign_out').click()
				else:
					print('登录失败')
					driver.save_screenshot('F:\\PyProjects\\maizi_login.png')
			except:
				pass
if __name__ == '__main__':
	usr_list=[{'usrname':'maizi_test@139.com','pwd':'abc123456'},{'usrname':'maizi_test@139.com','pwd':'abc1234562'}]
	url = 'http://www.maiziedu.com'
	loged_url = 'http://www.maiziedu.com/home/?source=login'
	driver = webdriver.Firefox()
	login=Login(driver,url,usr_list,loged_url)
	login.login_opre()
	time.sleep(3)
	driver.quit()
  
  
  
############################################################知识点代码########################################################## 
#encoding:utf-8
# example of how to use https://github.com/SeleniumHQ/selenium/blob/master/py/selenium/webdriver/support/expected_conditions.py

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

import unittest

# dr = webdriver.PhantomJS('phantomjs')
dr = webdriver.Firefox()
# dr = webdriver.Chrome()
url = 'http://www.baidu.com'
search_text_field_id = 'kw'
dr.get(url)

class ECExample(unittest.TestCase):

  def test_title_is(self):
    ''' 判断title是否符合预期 '''
    title_is_baidu = EC.title_is(u'百度一下，你就知道')
    self.assertTrue(title_is_baidu(dr))

  def test_titile_contains(self):
    ''' 判断title是否包含预期字符 '''
    title_should_contains_baidu = EC.title_contains(u'百度')
    self.assertTrue(title_should_contains_baidu(dr))

  def test_presence_of_element_located(self):
    ''' 判断element是否出现在dom树 '''
    locator = (By.ID, search_text_field_id)
    search_text_field_should_present = EC.visibility_of_element_located(locator)

    ''' 动态等待10s，如果10s内element加载完成则继续执行下面的代码，否则抛出异常 '''
    WebDriverWait(dr, 10).until(EC.presence_of_element_located(locator))
    WebDriverWait(dr, 10).until(EC.visibility_of_element_located(locator))

    self.assertTrue(search_text_field_should_present(dr))

  def test_visibility_of(self):
    search_text_field = dr.find_element_by_id(search_text_field_id)
    search_text_field_should_visible = EC.visibility_of(search_text_field)
    self.assertTrue(search_text_field_should_visible('yes'))

  def test_text_to_be_present_in_element(self):
    text_should_present = EC.text_to_be_present_in_element((By.NAME, 'tj_trhao123'), 'hao123')
    self.assertTrue(text_should_present(dr))


  @classmethod
  def tearDownClass(kls):
    print 'after all test'
    dr.quit()
    print 'quit dr'

if __name__ == '__main__':
  unittest.main()
