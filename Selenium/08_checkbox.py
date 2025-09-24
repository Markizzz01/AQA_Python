# Selenium. Check box

from selenium import webdriver  # импортируем WebDriver из Selenium
import time  # импортируем модуль time для задержки

driver = webdriver.Chrome()  # запускаем браузер Chrome
driver.get("https://demoqa.com/checkbox")  # открываем страницу с чекбоксами

checkbox_ladel = driver.find_element("xpath", "//label[@for='tree-node-home']")  # ищем label, связанный с чекбоксом "Home"
checkbox_ladel.click()  # кликаем по label (он визуально заменяет скрытый чекбокс)

checkbox_imput = driver.find_element("xpath", "//input[@id='tree-node-home']")  # ищем сам input-чекбокс "Home"
assert checkbox_imput.is_selected()  # проверяем, что чекбокс действительно выбран

time.sleep(3)  # ждём 3 секунды, чтобы увидеть результат
driver.quit()  # закрываем браузер