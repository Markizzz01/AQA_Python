# Работа с текстовыми полями и клавиатурой (send_keys, clear, assert, Keys)

# ДЗ Закрепите пройденный материал на сайте https://demoqa.com/text-box
# 1. Заполните все текстовые поля данными (почистить поля перед заполнением).
# 2. Проверьте, что данные действительно введены, используя **get_attribute()** и **assert**.


from selenium import webdriver # Импортируем WebDriver для управления браузером
import time # Импортируем time для использования задержек

driver = webdriver.Chrome()  # Создаём объект драйвера для Chrome
driver.get("https://demoqa.com/text-box") # Открываем нужную страницу

email_locator = driver.find_element ("xpath", "//input[@id='userEmail']") # Находим поле ввода email по XPath

email_locator.clear() # Очищаем поле от возможного текста
assert email_locator.get_attribute("value") == "", "Поле не пустое!"  # Проверяем, что поле действительно пустое

email_locator.send_keys("lesha.egorushkovv@yandex.ru") # Вводим текст в поле

assert email_locator.get_attribute("value") == "lesha.egorushkovv@yandex.ru", "Текст не введен правильно!" # Проверяем, что текст введён корректн

time.sleep(5)  # Пауза на 5 секунд, чтобы увидеть результат в браузере перед закрытием
driver.quit()  # Закрывает браузер и завершает работу драйвера
