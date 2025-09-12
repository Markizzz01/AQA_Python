# Ожидания в Selenium WebDriver: явные и неявные

from selenium import webdriver                              # Импортируем модуль для работы с браузером
from selenium.webdriver.common.by import By                 # Импортируем By для создания локаторов
from selenium.webdriver.support.ui import WebDriverWait     # Импортируем WebDriverWait для явных ожиданий
from selenium.webdriver.support import expected_conditions as EC  # Импортируем условия ожидания (кликабельность, видимость и т.д.)

driver = webdriver.Chrome()                                  # Создаём объект браузера Chrome
driver.get("https://demoqa.com/dynamic-properties")          # Открываем страницу demoqa с динамическими кнопками

wait = WebDriverWait(driver, 10, poll_frequency=1)          # Создаём явное ожидание: ждём до 10 секунд, проверяем каждую секунду

WILL_ENABLE = (By.ID, "enableAfter")                        # Определяем локатор кнопки, которая станет активной через 5 секунд
wait.until(EC.element_to_be_clickable(WILL_ENABLE))         # Дожидаемся, пока кнопка станет кликабельной

driver.find_element(*WILL_ENABLE).click()                   # Находим кнопку и кликаем (распаковываем кортеж через *)

driver.quit()                                               # Закрываем браузер после выполнения действий