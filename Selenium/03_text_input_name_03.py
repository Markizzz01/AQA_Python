# Работа с текстовыми полями и клавиатурой (send_keys, clear, assert, Keys)

# ДЗ Закрепите пройденный материал на сайте https://demoqa.com/text-box
# 1. Заполните все текстовые поля данными (почистить поля перед заполнением).
# 2. Проверьте, что данные действительно введены, используя **get_attribute()** и **assert**.

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")

fullName_field = driver.find_element("xpath","//input[@id='userName']")
fullName_field.clear()
assert fullName_field.get_attribute("value") == ""

fullName_field.send_keys("Alexey")
assert fullName_field.get_attribute("value") == "Alexey"

time.sleep(5)
driver.quit()

