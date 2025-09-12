# Selenium: User-agent & Alert

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# -------------------- Настройка браузера --------------------
options = webdriver.ChromeOptions()

# Устанавливаем кастомный User-Agent (маскируем браузер под обычного пользователя)
options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36")

# Отключаем режим автоматизации (чтобы сайт не понял, что это WebDriver)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# Запускаем браузер с этими настройками
driver = webdriver.Chrome(options=options)

# Создаём объект явного ожидания (ждать до 10 секунд, проверка каждые 1 сек)
wait = WebDriverWait(driver, 10, poll_frequency=1)

# -------------------- Открываем страницу с алертами --------------------
driver.get("https://demoqa.com/alerts")

# -------------------- 1. Простой alert --------------------
# Эта кнопка вызывает простое сообщение "You clicked a button"
alert_button = wait.until(EC.element_to_be_clickable(("xpath", "//button[@id='alertButton']")))
alert_button.click()                           # кликаем на кнопку
alert = wait.until(EC.alert_is_present())      # ждём появления alert
alert.accept()                                 # нажимаем "OK" (accept = подтвердить)

# -------------------- 2. Confirm alert --------------------
# Эта кнопка вызывает confirm alert с выбором: OK или Cancel
confirm_button = wait.until(EC.element_to_be_clickable(("xpath", "//button[@id='confirmButton']")))
confirm_button.click()
alert = wait.until(EC.alert_is_present())
alert.dismiss()                                # нажимаем "Cancel" (dismiss = отклонить)

# -------------------- 3. Prompt alert --------------------
# Эта кнопка вызывает prompt alert (можно ввести текст)
prompt_button = wait.until(EC.element_to_be_clickable(("xpath", "//button[@id='promtButton']")))
prompt_button.click()
alert = wait.until(EC.alert_is_present())
alert.send_keys("Alexey")                      # вводим текст в поле alert
alert.accept()                                 # нажимаем "OK" (accept)

# -------------------- Закрываем браузер --------------------
driver.quit()