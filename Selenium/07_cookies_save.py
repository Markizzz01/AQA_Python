import json  # Работа с JSON для сохранения и чтения cookies
import time  # Работа с задержками (sleep)
from selenium import webdriver  # Импорт Selenium для управления браузером

driver = webdriver.Chrome()  # Запуск браузера Chrome
driver.get("https://demoqa.com/login")  # Переход на страницу логина

# Локаторы полей и кнопки
USERNAME_FIELD = ("id", "userName")  # Поле ввода имени пользователя
PASSWORD_FIELD = ("id", "password")  # Поле ввода пароля
SUBMIT_BUTTON = ("id", "login")      # Кнопка "Войти"

# Ввод данных и клик по кнопке
driver.find_element(*USERNAME_FIELD).send_keys("testuser")  # Вводим логин
driver.find_element(*PASSWORD_FIELD).send_keys("Abc123$!")  # Вводим пароль
driver.find_element(*SUBMIT_BUTTON).click()                # Нажимаем кнопку "Войти"

time.sleep(2)  # Ждём 2 секунды, чтобы куки успели установиться

# Получаем все куки после авторизации
cookies = driver.get_cookies()  # cookies — это список словарей с данными о каждой куке

# Сохраняем куки в файл cookies.json
with open("cookies.json", "w") as file:
    json.dump(cookies, file, indent=4)  # Запись списка cookies в JSON файл с отступами

print("Cookies сохранены в cookies.json")  # Выводим сообщение о сохранении

driver.quit()  # Закрываем браузер