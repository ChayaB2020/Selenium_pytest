#shifting to child window
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com//windows")
driver.fullscreen_window()
driver.implicitly_wait(3)
driver.find_element(By.LINK_TEXT, "Click Here").click()
windows=driver.window_handles
driver.switch_to.window(windows[1])
#time.sleep(2)
print(driver.find_element(By.TAG_NAME,'h3').text)
driver.switch_to.window(windows[0])
#time.sleep(3)
print(driver.find_element(By.TAG_NAME,'h3').text)
#time.sleep(1)


