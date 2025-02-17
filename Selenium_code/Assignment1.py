#opening child window assignment

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com//loginpagePractise//")
driver.find_element(By.XPATH,'//a[@class="blinkingText"][1]').click()
wait=WebDriverWait(driver,5)
tabsOpened=driver.window_handles
driver.switch_to.window(tabsOpened[1])
email_id=wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR,"div[class='col-md-8'] p strong a"))).text
#time.sleep(2)
driver.switch_to.window(tabsOpened[0])
driver.find_element(By.ID,'username').send_keys(email_id)
#time.sleep(2)
driver.find_element(By.ID, "password").send_keys("12345")
#time.sleep(1)
driver.find_element(By.ID,"terms").click()
#time.sleep(1)
driver.find_element(By.ID, "signInBtn").click()
#time.sleep(2)
print(wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger"))))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)


