# Selenium. Home work — процесс фильтрации товаров, переход в карточку товара и разлогина

from selenium import webdriver                     # импортируем webdriver для управления браузером
from selenium.webdriver import ActionChains        # импортируем ActionChains для сложных действий
from selenium.webdriver.support.ui import WebDriverWait   # для явных ожиданий
from selenium.webdriver.support.select import Select      # для работы с выпадающими списками <select>
from selenium.webdriver.support import expected_conditions as EC  # готовые условия для ожиданий
import time                                        # модуль для пауз (sleep)

options = webdriver.ChromeOptions()                # создаем объект настроек Chrome
options.add_argument("--incognito")                # запускаем Chrome в режиме инкогнито
options.add_argument("--window-size=2560,1600")    # задаем размер окна браузера
options.add_experimental_option("prefs", {         # отключаем менеджер паролей
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
})

driver = webdriver.Chrome(options=options)         # запускаем Chrome с этими настройками
action = ActionChains(driver)                      # объект для сложных действий
wait = WebDriverWait(driver, 10)                   # объект для явных ожиданий (до 10 сек)

# Локаторы
USERNAME_FIELD = ("xpath", "//input[@id='user-name']")        # поле для логина
PASSWORD_FIELD = ("xpath", "//input[@id='password']")         # поле для пароля
LOGIN_BUTTON = ("xpath", "//input[@id='login-button']")       # кнопка "Login"
HEADER_TITLE = ("xpath", "//span[@class='title']")            # заголовок страницы
FILTER_BUTTON = ("xpath", "//select[@class='product_sort_container']")  # выпадающий список фильтра
PRODUCT_BUTTON = ("xpath", "//a[@id='item_2_title_link']")    # ссылка на карточку товара
BACK_BUTTON = ("xpath", "//button[@id='back-to-products']")   # кнопка "Back to products"
MENU_BUTTON = ("xpath", "//button[@id='react-burger-menu-btn']")  # кнопка "бургер-меню"
LOGOUT_BUTTON = ("xpath", "//a[@id='logout_sidebar_link']")   # кнопка "Logout" в меню

driver.get("https://www.saucedemo.com")            # открываем сайт
driver.find_element(*USERNAME_FIELD).clear()       # очищаем поле логина
driver.find_element(*USERNAME_FIELD).send_keys("standard_user")  # вводим логин
driver.find_element(*PASSWORD_FIELD).clear()       # очищаем поле пароля
driver.find_element(*PASSWORD_FIELD).send_keys("secret_sauce")   # вводим пароль
driver.find_element(*LOGIN_BUTTON).click()         # жмем "Login"

header = driver.find_element(*HEADER_TITLE)        # получаем заголовок
assert header.text == "Products"                   # проверяем, что попали на Products

# Фильтрация товаров
dropdown = Select(driver.find_element(*FILTER_BUTTON))  # создаем объект Select
dropdown.select_by_value("lohi")                        # сортируем по цене Low → High

# Переход в карточку товара
driver.find_element(*PRODUCT_BUTTON).click()       # кликаем по товару
assert driver.find_element(*BACK_BUTTON).is_displayed() # проверяем, что есть кнопка "Back"

# Возврат на список товаров
driver.find_element(*BACK_BUTTON).click()          # кликаем "Back to products"
assert driver.find_element(*HEADER_TITLE).text == "Products"  # проверяем заголовок

# Разлогин
driver.find_element(*MENU_BUTTON).click()          # открываем меню (бургер)
wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON)).click()  # ждем и кликаем "Logout"
assert driver.find_element(*USERNAME_FIELD).is_displayed()     # проверяем, что поле логина появилось

time.sleep(3)                                     # ждем 3 секунды перед закрытием браузера