# Работа с текстовыми полями и клавиатурой (send_keys, clear, assert, Keys)

# ДЗ Закрепите пройденный материал на сайте https://demoqa.com/text-box
# 1. Заполните все текстовые поля данными (почистить поля перед заполнением).
# 2. Проверьте, что данные действительно введены, используя **get_attribute()** и **assert**.

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")

address_permanent = driver.find_element("xpath", "//textarea[@id='permanentAddress']")

address_permanent.clear()
assert address_permanent.get_attribute("value") == "", "Поле не пустое!"

address_permanent.send_keys("Илькино, а дальше сами ищите")

assert address_permanent.get_attribute("value") == "Илькино, а дальше сами ищите", "Текст не введен правильно!"

time.sleep(5)
driver.quit()
