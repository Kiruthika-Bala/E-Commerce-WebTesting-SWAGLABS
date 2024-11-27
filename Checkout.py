from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
driver= webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
print(driver.title)
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.NAME,"password").send_keys("secret_sauce")
driver.find_element(By.XPATH,"//input[@id='login-button']").click()


#search the desirable product
driver.find_element(By.XPATH, "//div[normalize-space()='Sauce Labs Bolt T-Shirt']").click()
driver.find_element(By.XPATH,"//button[@id='add-to-cart']").click()
driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']").click()


#Checkout and Verification
driver.find_element(By.XPATH,"//button[@id='checkout']").click()
driver.find_element(By.XPATH,"//input[@id='first-name']").send_keys("Kiruthika")
driver.find_element(By.XPATH,"//input[@id='last-name']").send_keys("B")
driver.find_element(By.XPATH,"//input[@id='postal-code']").send_keys("001")
driver.find_element(By.XPATH,"//input[@id='continue']").click()
quan = driver.find_element(By.XPATH,"//div[@class='cart_quantity']")
quantity= quan.text
exp_quan=1
if quantity == exp_quan:
    print("Quantity Test case passed")
else:
    print("Quantity is not matched with your order, Please check")
driver.find_element(By.XPATH,"//button[@id='finish']").click()

finish = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[normalize-space()='Thank you for your order!']")))

assert "Thank you for your order!" == finish.text
print(finish.text)





