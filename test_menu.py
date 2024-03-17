import time
from selenium import webdriver
from selenium.webdriver.common.by import By

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
menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
menu.click()
time.sleep(2)
link_about = driver.find_element(By.XPATH, "//*[@id='about_sidebar_link']")
link_about.click()

time.sleep(1)
driver.close()