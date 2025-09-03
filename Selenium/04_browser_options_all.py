##Опции и загрузка
# ДЗ - Напишите опции и запускайте любой сайт с ними, посмотрите взаимодействие.

from selenium import webdriver

options = webdriver.ChromeOptions() # Создаём объект с настройками для Chrome
options.add_argument("--headless=new")
options.add_argument("--window-size=1280,800")
options.page_load_strategy = 'eager'


driver = webdriver.Chrome(options=options) # Передаём опции в драйвер и запускаем браузер
driver.get("https://demoqa.com/upload-download") # Открываем тестовую страницу

print(driver.title) # Выводим заголовок страницы (текст внутри <title>)
print(driver.get_window_size()) # Проверяем реальный размер окна (должен быть 1280x800)
print(driver.current_url) # Выводим текущий URL, чтобы убедиться, что страница открылась

driver.quit() # Закрываем браузер

