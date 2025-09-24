#Selenium. Action Chains (Наведение на мен)


import time  # для пауз
from selenium import webdriver  # управление браузером
from selenium.webdriver.support.ui import WebDriverWait  # явные ожидания
from selenium.webdriver import ActionChains  # для действий мыши/клавиатуры
from selenium.webdriver.chrome.options import Options  # настройки браузера

# -------------------- Настройки браузера --------------------
options = Options()  # создаём объект с настройками браузера
options.add_argument("--window-size=1920,1080")  # задаём размер окна

driver = webdriver.Chrome(options=options)  # запускаем Chrome
wait = WebDriverWait(driver, 10, poll_frequency=1)  # явное ожидание до 10 секунд
action = ActionChains(driver)  # создаём объект для цепочек действий

# -------------------- Переходим на страницу --------------------
driver.get("https://demoqa.com/menu")  # открываем страницу с меню

# -------------------- Локаторы элементов меню --------------------
MAIN_ITEM = ("xpath", "//a[text()='Main Item 2']")  # первый элемент меню
SUB_LIST = ("xpath", "//a[text()='SUB SUB LIST »']")  # подменю
SUB_ITEM = ("xpath", "//a[text()='Sub Sub Item 2']")  # конечный элемент

# -------------------- Находим элементы --------------------
main_item_elem = driver.find_element(*MAIN_ITEM)
sub_list_elem = driver.find_element(*SUB_LIST)
sub_item_elem = driver.find_element(*SUB_ITEM)

# -------------------- Цепочка действий: наведение и клик --------------------
action.move_to_element(main_item_elem).pause(1) \
      .move_to_element(sub_list_elem).pause(1) \
      .click(sub_item_elem).perform()  # наведение и клик на конечный элемент

# -------------------- Проверка --------------------
assert sub_item_elem.is_displayed()  # проверяем, что элемент виден

# -------------------- Пауза и закрытие --------------------
time.sleep(3)  # визуальная пауза
driver.quit()  # закрываем браузер