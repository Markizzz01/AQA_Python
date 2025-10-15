# PyTest. Allure

import pytest
import allure
from allure_commons.types import Severity, AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Python_Course.Python_All import names


@allure.epic("DemoQA.com")
@allure.feature("Login")
@allure.story("Positive Authorization")
@pytest.mark.usefixtures("driver")
class TestDemoQAAuth:

    @pytest.mark.smoke
    @allure.title("Позитивный кейс авторизации на demoqa.com")
    @allure.severity(Severity.NORMAL)
    @allure.link(url="https://confluence.com", name="Documentation")
    def test_login_positive(self):
        with allure.step("Open page. Step 1"):
            self.driver.get("https://demoqa.com/login")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Login page",
                attachment_type=AttachmentType.PNG
            )

        with allure.step("User data input. Step 2"):
            self.driver.find_element("id", "userName").send_keys("testuser")
            self.driver.find_element("id", "password").send_keys("Abc123$!")
            self.driver.find_element("id", "login").click()

        with allure.step("Checking successful login. Step 3"):
            logout_button = self.driver.find_element("id", "submit")
            assert logout_button.is_displayed(), "Логин не удался!"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Success authorization",
                attachment_type=AttachmentType.PNG
            )

    @pytest.mark.smoke
    @allure.title("Негативный кейс авторизации на demoqa.com")
    @allure.severity(Severity.NORMAL)
    @allure.link(url="https://confluence.com", name="Documentation")
    def test_login_negative(self):
        with allure.step("Open page. Step 1"):
            self.driver.get("https://demoqa.com/login")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Login negative page",
                attachment_type=AttachmentType.PNG
            )

        with allure.step("User data input. Step 2"):
            self.driver.find_element("id", "userName").send_keys("test")
            self.driver.find_element("id", "password").send_keys("Abc123ee!")
            self.driver.find_element("id", "login").click()

        with allure.step("Checking unsuccessful login. Step 3"):
            wait = WebDriverWait(self.driver, 10)
            invalid_message = wait.until(EC.visibility_of_element_located(("id", "name")))
            assert invalid_message.is_displayed()
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Login negative result",
                attachment_type=AttachmentType.PNG
            )


@allure.epic("Accounts")
@allure.feature("Book Searc")
@allure.story("Search Positive")
@pytest.mark.usefixtures("driver")
class TestDemoQABook:

    @pytest.mark.smoke
    @allure.title("Позитивный кейс поиска книги на demoqa.com")
    @allure.severity(Severity.NORMAL)
    @allure.link(url="https://confluence.com", name="Documentation")
    def test_search_book(self):
        with allure.step("Open page. Step 1"):
            self.driver.get("https://demoqa.com/books")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Books page",
                attachment_type=AttachmentType.PNG
            )

        with allure.step("Search book. Step 2"):
            self.driver.find_element("id", "searchBox").send_keys("Git")


        with allure.step("Found book. Step 3"):
            wait = WebDriverWait(self.driver, 10)
            book = wait.until(EC.visibility_of_element_located(("id", "see-book-Git Pocket Guide")))
            assert book.is_displayed(), "Поиск не выдал результатов"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Books",
                attachment_type=AttachmentType.PNG
            )




    @pytest.mark.smoke
    @allure.title("Негативный кейс поиска книги на demoqa.com")
    @allure.severity(Severity.NORMAL)
    @allure.link(url="https://confluence.com", name="Documentation")
    def test_search_negative_book(self):
        with allure.step("Open page. Step 1"):
            self.driver.get("https://demoqa.com/books")
            allure.attach(
               body=self.driver.get_screenshot_as_png(),
               name="Books page 2",
               attachment_type=AttachmentType.PNG
            )


        with allure.step("Search book.Step 2"):
            self.driver.find_element("id", "searchBox").send_keys("Книга,которой нет")

        with allure.step("Found book. Step 3"):
           wait = WebDriverWait(self.driver, 10)
           book = wait.until(EC.visibility_of_element_located(("xpath", "//div[text()='No rows found']")))
           assert book.is_displayed(), "Поиск не выдал результатов"
           allure.attach(
              body=self.driver.get_screenshot_as_png(),
              name="Books negative",
              attachment_type=AttachmentType.PNG
           )




