#Selenium. Action Chains (CLICK BUTTON)

#Selenium. Action Chains (CLICK BUTTON)

import time  # для паузы
from selenium import webdriver  # управление браузером
from selenium.webdriver.support.ui import WebDriverWait  # явные ожидания
from selenium.webdriver import ActionChains  # для действий мыши/клавиатуры
from selenium.webdriver.chrome.options import Options  # настройки браузера

options = Options()  # создаём объект с настройками браузера
options.add_argument("--window-size=1920,1080") # задаём размер окна браузера


driver = webdriver.Chrome(options=options)  # запускаем Chrome с заданными настройками
wait = WebDriverWait(driver, 10, poll_frequency=1)  # создаём объект ожидания (10 сек)
action = ActionChains(driver)  # создаём объект для цепочки действий

driver.get("https://demoqa.com/buttons")  # открываем страницу с кнопками
CLICK_ME_BUTTON = ("xpath", "//button[text()='Click Me']")  # локатор кнопки "Click Me"

BUTTON = driver.find_element(*CLICK_ME_BUTTON)  # ищем кнопку
action.click(BUTTON).perform()  # выполняем клик по кнопке

message = driver.find_element("id", "dynamicClickMessage")  # ищем сообщение после клика
assert message.text == "You have done a dynamic click"  # проверяем правильность сообщения

time.sleep(4)  # ждём, чтобы увидеть результат
driver.quit()  # закрываем браузер