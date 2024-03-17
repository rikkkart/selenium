import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, "//*[@id='user-name']")
user_name.send_keys(login_standard_user)
user_name.send_keys(Keys.BACKSPACE)
time.sleep(2)
user_name.send_keys(Keys.BACKSPACE)
time.sleep(2)
user_name.send_keys("er")

# password = driver.find_element(By.CSS_SELECTOR, "#password")
# password.send_keys(password_all)
# button_login = driver.find_element(By.XPATH, "//*[@id='login-button']")
# button_login.click()


time.sleep(2)
driver.close()