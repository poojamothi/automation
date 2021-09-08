from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests


PATH='C:\Program Files (x86)\chromedriver.exe'
driver=webdriver.Chrome(PATH)
driver.get('http://164.100.69.66/jsearch/')
btn=driver.find_element_by_name("Submit4")
btn.send_keys(Keys.RETURN)

frame = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "dynfr"))
)
driver.switch_to.frame(frame)
s=driver.find_element_by_name('p_name')
s.send_keys(" ")

s2=driver.find_element_by_name('frdate')
h=driver.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[4]/td[2]/img').click()
h1=driver.find_element_by_xpath('//*[@id="scwMonths"]').click()
h2=driver.find_element_by_xpath('//*[@id="scwMonths"]/option[7]').click()
h3=driver.find_element_by_xpath('//*[@id="scwCell_3"]').click()

s3=driver.find_element_by_name('todate')
H=driver.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[5]/td[2]/img').click()
H1=driver.find_element_by_xpath('//*[@id="scwMonths"]').click()
H2=driver.find_element_by_xpath('//*[@id="scwMonths"]/option[7]').click()
H3=driver.find_element_by_xpath('//*[@id="scwCell_30"]').click()
s4=driver.find_element_by_name('Submit')
s4.send_keys(Keys.RETURN)

time.sleep(2)

r=driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[1]/td[3]/a').click()
