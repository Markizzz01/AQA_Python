# Опции и загрузка
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)
driver.get("https://demoqa.com/upload-download")

print(driver.title)
