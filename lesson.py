import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
driver.get(('https://www.saucedemo.com/'))
driver.maximize_window()
#user_name = driver.find_element(By.ID, "user-name")
user_name = driver.find_element(By.XPATH, "//*[@id='user-name']")
user_name.send_keys("standard_user")
password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys("secret_sauce")
button_login = driver.find_element(By.XPATH, "//*[@id='login-button']")
button_login.click()
time.sleep(5)
driver.close()