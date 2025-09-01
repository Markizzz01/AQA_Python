# Работа с текстовыми полями и клавиатурой (send_keys, clear, assert, Keys)

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")

fullName_field = driver.find_element("xpath","//input[@id='userName']")
fullName_field.clear()
assert fullName_field.get_attribute("value") == ""

fullName_field.send_keys("Alex")
assert fullName_field.get_attribute("value") == "Alex"

time.sleep(5)
driver.quit()