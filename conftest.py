# Фикстура (глобально для всех тестов)

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver(request):
    chrome_options = Options()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size=2560,1600")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)

    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture(autouse=True)
def setup_environment_properties():
    properties = {
        "STAGE": "AQA",
        "BROWSER": "Chrome"
    }
    with open("allure-results/environment.properties", "w") as file:
        for key, value in properties.items():
            file.write(f"{key}={value}\n")