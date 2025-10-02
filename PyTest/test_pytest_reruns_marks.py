# Практика PyTest и Selenium: Перезапуск, остановка и маркировка тестов
import random  # можно использовать для флаки-тестов с случайными значениями
import pytest  # импортируем pytest для написания тестов и использования маркеров
from selenium import webdriver  # импортируем драйвер для управления браузером


class TestDemoQAFlow:

    def setup_method(self):  # Предусловие: выполняется перед каждым тестом
        options = webdriver.ChromeOptions()  # создаем объект с настройками Chrome
        options.add_argument("--incognito")  # включаем режим инкогнито
        options.add_argument("--window-size=2560,1600")  # задаем размер окна браузера
        self.driver = webdriver.Chrome(options=options)  # создаем экземпляр драйвера Chrome

    @pytest.mark.smoke  # маркируем тест как smoke
    def test_login_page(self):  # тест: логин и открытие страницы
        self.driver.get("https://demoqa.com/login")  # открываем страницу логина
        assert self.driver.current_url == "https://demoqa.com/login", "Ошибка URL"  # проверяем URL страницы

    @pytest.mark.regression  # маркируем тест как regression
    def test_open_books_page(self):
        self.driver.get("https://demoqa.com/books")  # открываем страницу книг
        assert self.driver.current_url == "https://demoqa.com/books", "Ошибка URl"  # проверяем URL

    @pytest.mark.smoke  # маркируем тест как smoke
    @pytest.mark.sanity  # маркируем тест как sanity
    def test_open_page(self):
        self.driver.get("https://demoqa.com/profile")  # открываем страницу профиля
        assert self.driver.current_url == "https://demoqa.com/profile", "Ошибкааа,стой,убьет"  # проверяем URL

    def teardown_method(self):  # Постусловие: закрытие браузера после теста
        self.driver.close()  # закрываем текущее окно браузера


class TestDemoQAFlowFlaky:  # Флаки-тест: тест, который может намеренно падать
    @pytest.mark.smoke  # маркируем тест как smoke
    def setup_method(self):  # Предусловие: перед тестом
        self.driver = webdriver.Chrome()  # создаем экземпляр драйвера Chrome

    @pytest.mark.smoke  # маркируем тест как smoke
    def test_always_fail(self):
        assert False, "Тест падает намеренно"  # этот тест всегда падает для демонстрации reruns

    def teardown_method(self):  # Постусловие: закрытие браузера после теста
        self.driver.quit()  # полностью закрываем браузер