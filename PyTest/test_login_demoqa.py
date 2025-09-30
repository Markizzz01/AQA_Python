# Практика PyTest и Selenium: логин и форма на DemoQA

from selenium import webdriver  # импортируем драйвер для управления браузером
from selenium.webdriver.support.ui import WebDriverWait  # импортируем явные ожидания
from selenium.webdriver.support import expected_conditions as EC  # импорт условий для ожиданий


class TestDemoQAFlow:

    def setup_method(self):  # Предусловие: выполняется перед каждым тестом
        options = webdriver.ChromeOptions()  # создаем объект с настройками Chrome
        options.add_argument("--incognito")  # включаем режим инкогнито
        options.add_argument("--window-size=2560,1600")  # задаем размер окна браузера
        self.driver = webdriver.Chrome(options=options)  # создаем экземпляр драйвера Chrome
        self.wait = WebDriverWait(self.driver, 10)  # создаем объект WebDriverWait с таймаутом 10 секунд

    def test_login_and_text_box(self):  # тест: логин и заполнение формы
        self.driver.get("https://demoqa.com/login")  # открываем страницу логина
        assert self.driver.current_url == "https://demoqa.com/login", "Ошибка URL"  # проверяем URL страницы

        self.driver.find_element("id", "userName").send_keys("testuser")  # вводим имя пользователя
        self.driver.find_element("id", "password").send_keys("Abc123$!")  # вводим пароль
        self.driver.find_element("id", "login").click()  # нажимаем кнопку Login

        logout_button = self.wait.until(EC.visibility_of_element_located(("id", "submit")))  # ждём появления кнопки logout
        assert logout_button.is_displayed(), "Логин не удался!"  # проверяем, что кнопка видна (логин успешный)

        self.driver.get("https://demoqa.com/text-box")  # открываем страницу с формой Text Box
        assert self.driver.current_url == "https://demoqa.com/text-box", "Ошибка URL"  # проверяем URL формы

        self.driver.find_element("id", "userName").send_keys("Abibas")  # вводим имя
        self.driver.find_element("id", "userEmail").send_keys("Abibas@gmail.com")  # вводим email
        self.driver.find_element("id", "currentAddress").send_keys("Москва, улица немая, дом2")  # вводим текущий адрес
        self.driver.find_element("id", "permanentAddress").send_keys("Test")  # вводим постоянный адрес
        self.driver.find_element("id", "submit").click()  # нажимаем Submit

        output = self.driver.find_element("id", "output")  # находим блок вывода данных
        assert output.is_displayed(), "Блок вывода не отображается"  # проверяем видимость блока
        assert "Abibas" in output.text  # проверяем, что имя отображается в блоке
        assert "Abibas@gmail.com" in output.text  # проверяем email
        assert "Москва, улица немая, дом2" in output.text  # проверяем текущий адрес
        assert "Test" in output.text  # проверяем постоянный адрес

    def test_search_book(self):  # тест: поиск книги
        self.driver.get("https://demoqa.com/books")  # открываем страницу с книгами
        assert self.driver.current_url == "https://demoqa.com/books", "Ошибка URL"  # проверяем URL

        self.driver.find_element("id", "searchBox").send_keys("Git")  # вводим текст для поиска

        book = self.wait.until(EC.visibility_of_element_located(("id", "see-book-Git Pocket Guide")))  # ждём появления книги
        print("Найденная книга:", book.text)  # выводим название найденной книги в консоль
        assert book.is_displayed(), "Поиск не выдал результатов"  # проверяем, что книга видна


class TestDemoQAFlowNegative:

    def setup_method(self):  # Предусловие: выполняется перед каждым негативным тестом
        options = webdriver.ChromeOptions()  # создаем объект с настройками Chrome
        options.add_argument("--incognito")  # режим инкогнито
        options.add_argument("--window-size=2560,1600")  # размер окна
        self.driver = webdriver.Chrome(options=options)  # создаем драйвер
        self.wait = WebDriverWait(self.driver, 10)  # объект ожиданий

    def test_login_negative(self):  # тест на неверный логин
        self.driver.get("https://demoqa.com/login")  # открываем страницу логина
        assert self.driver.current_url == "https://demoqa.com/login", "Ошибка URL"  # проверяем URL

        self.driver.find_element("id", "userName").send_keys("a.egorushkov")  # вводим неправильное имя
        self.driver.find_element("id", "password").send_keys("qwerty")  # вводим неправильный пароль
        self.driver.find_element("id", "login").click()  # нажимаем Login

        invalid_message = self.wait.until(EC.visibility_of_element_located(("id", "name")))  # ждём появления сообщения об ошибке
        assert invalid_message.is_displayed(), "Сообщение 'Invalid username or password!' не появилось"  # проверяем отображение ошибки

    def test_search_book_negative(self):  # тест поиска несуществующей книги
        self.driver.get("https://demoqa.com/books")  # открываем страницу книг
        self.driver.find_element("id", "searchBox").send_keys("negative")  # ищем несуществующую книгу

        no_rows_message = self.driver.find_element("xpath", "//div[text()='No rows found']")  # находим сообщение о пустом результате
        assert no_rows_message.is_displayed(), "Сообщение 'No rows found' не появилось"  # проверяем отображение сообщения

    def teardown_method(self):  # Постусловие: выполняется после каждого теста
        self.driver.quit()  # закрываем браузер