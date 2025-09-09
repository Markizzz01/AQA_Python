# Загрузка файлов
# ДЗ - Создайте в проекте файл и загрузить его.
# Страница для выполнения задания: https://demoqa.com/upload-download

from selenium import webdriver  # Импортируем модуль webdriver из Selenium для управления браузером
import time  # Импортируем модуль time для использования задержек

options = webdriver.ChromeOptions()  # Создаём объект с настройками для Chrome
options.add_argument("--incognito")  # Добавляем режим инкогнито, чтобы не сохранялись куки и история

driver = webdriver.Chrome(options=options)  # Запускаем Chrome с указанными настройками
driver.get("https://demoqa.com/upload-download")  # Открываем страницу с формой загрузки файлов

upload_file_field = driver.find_element("xpath","//input[@id='uploadFile']") # Находим поле для загрузки файла по XPath (элемент input с id="uploadFile")
upload_file_field.send_keys(r"/Users/lesaegoruskov/PycharmProjects/AQA_Python/Python_Course/info.txt") # Передаем путь к файлу в поле загрузки, r"" используется для raw-строки, чтобы обратные слэши не интерпретировались как спецсимволы
uploaded_file_path = driver.find_element("id", "uploadedFilePath").text # Получаем текст из элемента с id="uploadedFilePath"

print(uploaded_file_path)  # Выводим на консоль путь к загруженному файлу (подтверждение, что файл выбран)

time.sleep(5)  # Пауза в 5 секунд, чтобы можно было увидеть изменения на странице перед закрытием браузера
driver.quit()  # Закрываем браузер и завершаем сессию Selenium



from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options)
driver.get("https://demoqa.com/upload-download")

upload_file_field = driver.find_element("xpath","//input[@id='uploadFile']")
upload_file_field.send_keys(r"/Users/lesaegoruskov/PycharmProjects/AQA_Python/Python_Course/Снимок экрана 2025-08-25 в 11.50.01.png")

time.sleep(5)
driver.quit()

# Если у поля есть атрибут multiple, то можно загрузить несколько файлов сразу — просто передав список файлов в send_keys, разделённых пробелом.
# В ином случае последовательно
