import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver= webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
print(driver.title)
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.NAME,"password").send_keys("secret_sauce")
driver.find_element(By.XPATH,"//input[@id='login-button']").click()
time.sleep(5)

#search the desirable product
driver.find_element(By.XPATH, "//div[normalize-space()='Sauce Labs Bolt T-Shirt']").click()
driver.find_element(By.XPATH,"//button[@id='add-to-cart']").click()
driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']").click()
time.sleep(5)