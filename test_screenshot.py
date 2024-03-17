
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

driver = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, "//*[@id='user-name']")
user_name.send_keys(login_standard_user)
password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys(password_all)
button_login = driver.find_element(By.XPATH, "//*[@id='login-button']")
button_login.click()
# url = "https://www.saucedemo.com/inventory.html"
# get_url = driver.current_url
# print(get_url)
#
# assert url ==get_url
# print("good url")
time.sleep(2)
now_date = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

name_screenshot = 'screenshot' + now_date + '.png'
driver.save_screenshot('C:\\Users\\user\\PycharmProjects\\selenium\\screen\\' + name_screenshot)

time.sleep(2)
driver.close()