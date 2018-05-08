#coding=utf-8
from selenium import webdriver
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
		time.sleep(2)
		login_btn = self.driver.find_element_by_link_text('登录')
		usr_ele = self.driver.find_element_by_id('id_account_l')
		pwd_ele = self.driver.find_element_by_id('id_password_l')
		login_ok = self.driver.find_element_by_id('login_btn')
		time.sleep(2)
		
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
					driver.save_screenshot('F:\\PyProjects\\maizi_login.png') #登录失败截取对应的屏幕
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
