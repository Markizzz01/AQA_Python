#Selenium. Action Chains (Double click)

import time  # для паузы
from selenium import webdriver  # управление браузером
from selenium.webdriver.support.ui import WebDriverWait  # явные ожидания
from selenium.webdriver import ActionChains  # для действий мыши/клавиатуры
from selenium.webdriver.chrome.options import Options  # настройки браузера

options = Options()  # создаём объект с настройками браузера
options.add_argument("--window-size=1920,1080")  # задаём размер окна браузера

driver = webdriver.Chrome(options=options)  # запускаем Chrome с заданными настройками
wait = WebDriverWait(driver, 10, poll_frequency=1)  # ждём до 10 секунд при поиске элементов
action = ActionChains(driver)  # создаём объект для цепочки действий (мышь/клавиатура)

driver.get("https://demoqa.com/buttons")  # открываем страницу с кнопками

DB_BUTTON_LOCATOR = ("xpath", "//button[@id='doubleClickBtn']")  # локатор кнопки для двойного клика
BUTTON = driver.find_element(*DB_BUTTON_LOCATOR)  # ищем кнопку по локатору и сохраняем в переменную

action.double_click(BUTTON).perform()  # выполняем двойной клик по кнопке

time.sleep(3)  # ждём 3 секунды, чтобы увидеть результат
driver.quit()  # закрываем браузер