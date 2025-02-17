#handling dropdown
import time
from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By


#service_obj=Service(executable_path="D://Chaya//chromedriver.exe")
driver=webdriver.Chrome() #service=service_obj)
driver.get("https://rahulshettyacademy.com//dropdownsPractise//")
driver.fullscreen_window()
driver.find_element(By.ID,"autosuggest").send_keys("US")
time.sleep(2)
countries=driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']/a")
for ele in countries:
    if ele.text== 'Austria':
        ele.click()
        break

assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == 'Austria'
time.sleep(2)
driver.close()