import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver= webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
print(driver.title)
#Submitting login page
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.NAME,"password").send_keys("secret_sauce")
driver.find_element(By.XPATH,"//input[@id='login-button']").click()
time.sleep(5)
