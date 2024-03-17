import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://www.selenium.dev/documentation/webdriver/interactions/windows/'
driver.get(base_url)


time_09_03_2024 = driver.find_element(By.XPATH, '//div[contains(@class, "react-datepicker__day--today")]')
time.sleep(2)
check_box.click()
# user_name.send_keys(login_standard_user)
# password = driver.find_element(By.CSS_SELECTOR, "#password")
# password.send_keys(password_all)
# button_login = driver.find_element(By.XPATH, "//*[@id='login-button']")
# button_login.click()
# # url = "https://www.saucedemo.com/inventory.html"
# # get_url = driver.current_url
# # print(get_url)
# #
# # assert url ==get_url
# # print("good url")

time.sleep(2)
