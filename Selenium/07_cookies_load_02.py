import json
from selenium import webdriver
import time

# Запускаем браузер
driver = webdriver.Chrome()
driver.get("https://demoqa.com/login")

# Очищаем все куки на странице
driver.delete_all_cookies()

# Загружаем куки из файла cookies.json
with open("cookies.json", "r") as file:
    cookies = json.load(file)

# Добавляем каждую куку в браузер
for cookie in cookies:
    driver.add_cookie(cookie)

# Обновляем страницу, чтобы авторизация сработала
driver.refresh()

# Ждём пару секунд, чтобы убедиться, что вошли
time.sleep(3)

print("Авторизация через cookies выполнена")

driver.quit()