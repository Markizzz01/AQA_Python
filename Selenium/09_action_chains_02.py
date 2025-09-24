#Selenium. Action Chains (RIGHT CLICK BUTTON)

import time  # для паузы
from selenium import webdriver  # управление браузером
from selenium.webdriver.support.ui import WebDriverWait  # явные ожидания
from selenium.webdriver import ActionChains  # для действий мыши/клавиатуры
from selenium.webdriver.chrome.options import Options  # настройки браузера

options = Options()  # создаём объект с настройками браузера
options.add_argument("--window-size=1920,1080")  # задаём размер окна браузера

driver = webdriver.Chrome(options=options)  # запускаем Chrome с заданными настройками
wait = WebDriverWait(driver, 10, poll_frequency=1)  # создаём объект ожидания (10 сек)
action = ActionChains(driver)  # создаём объект для цепочки действий с мышкой/клавиатурой

driver.get("https://demoqa.com/buttons")  # открываем страницу с кнопками
RIGHT_CLICK_BUTTON = ("xpath",  "//button[@id='rightClickBtn']")  # локатор кнопки "Right Click Me"

BUTTON = driver.find_element(*RIGHT_CLICK_BUTTON)  # ищем элемент кнопки
action.context_click(BUTTON).perform()  # выполняем клик правой кнопкой по найденному элементу

message = driver.find_element("id", "rightClickMessage")  # ищем сообщение после клика
assert message.text == "You have done a right click"  # проверяем, что появилось правильное сообщение

time.sleep(4)  # ждём 4 секунды, чтобы увидеть результат
driver.quit()  # закрываем браузер