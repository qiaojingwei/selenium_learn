from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get('https://mail.163.com')
# WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="lbNormal')))

driver.find_element_by_xpath('//*[@id="lbNormal"]').click()

#使用iframe标签中的id值进行切换
driver.switch_to.frame('x-URS-iframe')

#标签数从1开始计数，div[1],div[2]......
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/input').send_keys('111')
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/form/div/div[3]/div[2]/input[2]').send_keys('222')
print(driver.title)
