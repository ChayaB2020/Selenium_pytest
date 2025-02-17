from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
file_path="C:\\Users\\Mahesh\\Downloads\\download.xlsx"
fruit_name='Apple'

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com//upload-download-test//")
driver.fullscreen_window()
driver.implicitly_wait(5)
driver.find_element(By.ID, "downloadButton").click()


#Edit the excel sheet
#upload excel sheet
upload_file=driver.find_element(By.XPATH, "//input[@type='file']")
upload_file.send_keys(file_path)

#Verify upload is complete
wait= WebDriverWait(driver,5)
locator=(By.XPATH,"//div[@class='Toastify__toast-body']/div[2]")
wait.until(EC.visibility_of_element_located(locator))
print(driver.find_element(*locator).text)

#get the price column by using name of the item
price_column=driver.find_element(By.XPATH,"//div[text()='Price']").get_attribute("data-column-id")
print(price_column)
actual_price=driver.find_element(By.XPATH, "//div[text()='"+fruit_name+"']/parent::div/parent::div/div[@id='cell-"+price_column+"-undefined']/div").text
print(actual_price)