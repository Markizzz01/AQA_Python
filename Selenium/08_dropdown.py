# Selenium. Dropdown

from selenium import webdriver
from selenium.webdriver.support.select import Select  # Импорт класса Select для работы с <select>
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")  # Открываем страницу с дропдауном

DROPDOWN_ELEMENT = ("xpath", "//select[@id='dropdown']")  # Локатор выпадающего списка
dropdown = Select(driver.find_element(*DROPDOWN_ELEMENT))  # Создаем объект Select для взаимодействия

dropdown.select_by_value("2")  # Выбираем пункт по value (Option 2)
time.sleep(4)  # Ждем, чтобы визуально увидеть выбор

dropdown.select_by_value("1") # Выбираем пункт по value (Option 1)
time.sleep(4) # Ждем, чтобы визуально увидеть выбор

driver.quit()  # Закрываем браузер