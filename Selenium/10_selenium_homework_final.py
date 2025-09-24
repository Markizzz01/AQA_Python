# Selenium. Home work —  процесс покупки

from selenium import webdriver          # импортируем webdriver для управления браузером
from selenium.webdriver import ActionChains  # импортируем ActionChains для сложных действий (hover, drag&drop и т.д.)
from selenium.webdriver.support.ui import WebDriverWait  # импортируем WebDriverWait для явных ожиданий
import time                             # импортируем time для паузы (sleep)

options = webdriver.ChromeOptions()     # создаем объект настроек Chrome
options.add_argument("--incognito")     # запускаем Chrome в режиме инкогнито
options.add_argument("--window-size=2560,1600")  # задаем размер окна браузера
options.add_experimental_option("prefs", {       # отключаем сервисы сохранения паролей
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
})

driver = webdriver.Chrome(options=options)  # создаем драйвер Chrome с заданными настройками
action = ActionChains(driver)               # создаем объект для выполнения действий с мышкой/клавой
wait = WebDriverWait(driver, 10)            # создаем объект для ожиданий (макс. 10 секунд)

# Локаторы (XPath и другие селекторы для элементов страницы)
USERNAME_FIELD = ("xpath", "//input[@id='user-name']")   # поле ввода логина
PASSWORD_FIELD = ("xpath", "//input[@id='password']")    # поле ввода пароля
LOGIN_BUTTON = ("xpath", "//input[@id='login-button']")  # кнопка входа
HEADER_TITLE = ("xpath", "//span[@class='title']")       # заголовок на страницах
ADD_BACKPACK = ("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']")  # кнопка "Add to cart" для рюкзака
ADD_BIKE_LIGHT = ("xpath", "//button[@id='add-to-cart-sauce-labs-bike-light']")  # кнопка "Add to cart" для фонарика
ADD_BOLT_TSHIRT = ("xpath", "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")  # кнопка "Add to cart" для футболки
CART_ICON = ("xpath", "//div[@id='shopping_cart_container']")   # иконка корзины
CART_COUNT = ("class name", "shopping_cart_badge")              # счетчик товаров в корзине
CHECKOUT_BUTTON = ("xpath", "//button[@id='checkout']")         # кнопка "Checkout"
FIRST_NAME = ("xpath", "//input[@id='first-name']")             # поле "First Name"
LAST_NAME = ("xpath", "//input[@id='last-name']")               # поле "Last Name"
POSTAL_CODE = ("xpath", "//input[@id='postal-code']")           # поле "Postal Code"
CONTINUE_BUTTON = ("xpath", "//input[@id='continue']")          # кнопка "Continue"
FINISH_BUTTON = ("xpath", "//button[@id='finish']")             # кнопка "Finish"
HOME_BUTTON = ("xpath", "//button[@id='back-to-products']")     # кнопка "Back to products"

driver.get("https://www.saucedemo.com")       # открываем сайт
driver.find_element(*USERNAME_FIELD).clear()  # очищаем поле логина
driver.find_element(*USERNAME_FIELD).send_keys("standard_user")  # вводим логин
driver.find_element(*PASSWORD_FIELD).clear()  # очищаем поле пароля
driver.find_element(*PASSWORD_FIELD).send_keys("secret_sauce")   # вводим пароль
driver.find_element(*LOGIN_BUTTON).click()    # жмем кнопку входа

header = driver.find_element(*HEADER_TITLE)   # находим заголовок
assert header.text == "Products"              # проверяем, что попали на страницу "Products"

driver.find_element(*ADD_BACKPACK).click()    # добавляем рюкзак в корзину
driver.find_element(*ADD_BIKE_LIGHT).click()  # добавляем фонарик в корзину
driver.find_element(*ADD_BOLT_TSHIRT).click() # добавляем футболку в корзину

cart_count = driver.find_element(*CART_COUNT) # находим счетчик корзины
assert cart_count.text == "3"                 # проверяем, что в корзине 3 товара

driver.find_element(*CART_ICON).click()       # кликаем по иконке корзины
header = driver.find_element(*HEADER_TITLE)   # снова получаем заголовок
assert header.text == "Your Cart"             # проверяем, что заголовок = "Your Cart"

driver.find_element(*CHECKOUT_BUTTON).click() # жмем кнопку Checkout
header = driver.find_element(*HEADER_TITLE)   # проверяем заголовок
assert header.text == "Checkout: Your Information"

driver.find_element(*FIRST_NAME).send_keys("Alexey")     # вводим имя
driver.find_element(*LAST_NAME).send_keys("Egorushkov")  # вводим фамилию
driver.find_element(*POSTAL_CODE).send_keys("123456")    # вводим индекс
driver.find_element(*CONTINUE_BUTTON).click()            # жмем кнопку Continue

header = driver.find_element(*HEADER_TITLE)   # снова проверяем заголовок
assert header.text == "Checkout: Overview"    # проверяем, что перешли на Overview

driver.find_element(*FINISH_BUTTON).click()   # жмем Finish
header = driver.find_element(*HEADER_TITLE)   # проверяем заголовок
assert header.text == "Checkout: Complete!"   # проверяем, что покупка завершена

driver.find_element(*HOME_BUTTON).click()     # жмем Back to products
header = driver.find_element(*HEADER_TITLE)   # проверяем заголовок
assert header.text == "Products"              # проверяем, что вернулись на Products

time.sleep(3)  # даем 3 секунды посмотреть результат перед закрытием браузера