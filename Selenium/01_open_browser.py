# Открытие сайтов через WebDriver

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")
time.sleep(5)
driver.quit()
