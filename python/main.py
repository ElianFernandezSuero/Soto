from selenium import webdriver
import time

driver = webdriver.Chrome()

login_url = "https://example.com/login"
driver.get(login_url)

username_field = driver.find_element("username")
password_field = driver.find_element("password")

username_field.send_keys("your_username")
password_field.send_keys("your_password")

login_button = driver.find_element_by_id("login-button")
login_button.click()

time.sleep(2)

driver.quit()
