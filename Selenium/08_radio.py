# Selenium. Radio buttons. Все кнопки.

from selenium import webdriver   # импортируем webdriver для управления браузером
import time                      # импортируем time для пауз

driver = webdriver.Chrome()      # открываем браузер Chrome
driver.get("https://demoqa.com/radio-button")  # переходим на страницу с радио-кнопками

# --- Локаторы для всех радио-кнопок ---
YES_BUTTON = ("xpath", "//input[@id='yesRadio']")       # input для проверки статуса
YES_LABEL = ("xpath", "//label[@for='yesRadio']")      # label для клика
IMPRESSIVE_BUTTON = ("xpath", "//input[@id='impressiveRadio']")
IMPRESSIVE_LABEL = ("xpath", "//label[@for='impressiveRadio']")
NO_BUTTON = ("xpath", "//input[@id='noRadio']")        # кнопка "No", disabled

# --- Работа с кнопкой "Yes" ---
driver.find_element(*YES_LABEL).click()                # кликаем по label
assert driver.find_element(*YES_BUTTON).is_selected()  # проверяем, что выбрано

# --- Работа с кнопкой "Impressive" ---
driver.find_element(*IMPRESSIVE_LABEL).click()               # кликаем по label
assert driver.find_element(*IMPRESSIVE_BUTTON).is_selected() # проверяем, что выбрано

# --- Работа с кнопкой "No" ---
assert not driver.find_element(*NO_BUTTON).is_enabled()   # проверяем, что кнопка disabled

time.sleep(5)   # пауза, чтобы увидеть результат
driver.quit()   # закрываем браузер