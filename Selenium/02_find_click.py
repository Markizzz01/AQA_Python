#  Поиск элемента по XPath и клик

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://hyperskill.org/")

logo = driver.find_element(By.XPATH, '//a[contains(@class, "nav_logo")]')
logo.click()

time.sleep(5)
driver.quit()
