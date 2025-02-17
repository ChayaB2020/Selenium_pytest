from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com//angularpractice//")
driver.implicitly_wait(3)

# CSS - a[href*='shop'] Xpath- //a[contains(@href='shop')]
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
time.sleep(1)
items_list=driver.find_elements(By.XPATH, '//div[@class="card h-100"]')
for ele in items_list:
    if ele.find_element(By.XPATH, 'div/h4/a').text == 'Blackberry':
        ele.find_element(By.XPATH, 'div/button').click()
        break
time.sleep(1)
driver.find_element(By.XPATH,'//a[@class="nav-link btn btn-primary"]').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, " button[class='btn btn-success']").click()
time.sleep(1)
driver.find_element(By.ID,'country').send_keys('ind')
#time.sleep(3)
wait=WebDriverWait(driver,6)
wait.until(ec.visibility_of_element_located((By.XPATH, '//div[@class="suggestions"]/ul/li/a')))
countries=driver.find_elements(By.XPATH, '//div[@class="suggestions"]/ul/li/a')
for country in countries:
    if country.text == 'India':
        country.click()
        break
time.sleep(1)
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(1)
print(driver.find_element(By.CSS_SELECTOR, '.alert-success').text)
#print(driver.find_element(By.XPATH, '//div[@class="alert alert-success alert-dismissible"]').text)
time.sleep(1)

