# Selenium. Action Chains (Drag & Drop)

import time  # для пауз
from selenium import webdriver  # управление браузером
from selenium.webdriver.support.ui import WebDriverWait  # явные ожидания
from selenium.webdriver import ActionChains  # для действий мыши/клавиатуры
from selenium.webdriver.chrome.options import Options  # настройки браузера

# -------------------- Настройки браузера --------------------
options = Options()  # создаём объект с настройками
options.add_argument("--window-size=1920,1080")  # задаём размер окна

driver = webdriver.Chrome(options=options)  # запускаем Chrome
wait = WebDriverWait(driver, 10, poll_frequency=1)  # явное ожидание до 10 секунд
action = ActionChains(driver)  # создаём объект цепочек действий

# -------------------- Переходим на страницу --------------------
driver.get("https://demoqa.com/droppable")  # открываем страницу с drag & drop

# -------------------- Локаторы элементов --------------------
SOURCE_LOCATOR = ("xpath", "//div[@id='draggable']")  # элемент, который перетаскиваем
TARGET_LOCATOR = ("xpath", "//div[@id='droppable']")  # зона, куда перетаскиваем

# -------------------- Находим элементы --------------------
source_elem = driver.find_element(*SOURCE_LOCATOR)  # находим элемент source
target_elem = driver.find_element(*TARGET_LOCATOR)  # находим элемент target

# -------------------- Цепочка действий: перетаскивание --------------------
action.drag_and_drop(source_elem, target_elem).perform()  # перетаскиваем source в target

# -------------------- Проверка --------------------
assert "Dropped!" in target_elem.text  # проверяем, что текст изменился после drop

# -------------------- Пауза и закрытие --------------------
time.sleep(3)  # визуальная пауза
driver.quit()  # закрываем браузер