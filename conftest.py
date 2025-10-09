# Фикстура (глобально для всех тестов)

import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)  # фикстура будет запускаться автоматически
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--window-size=2560,1600")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    request.cls.driver = driver   # присваиваем драйвер классу
    yield
    driver.quit()