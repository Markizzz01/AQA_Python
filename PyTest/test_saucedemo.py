import pytest
import allure
from allure_commons.types import Severity, AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("SauceDemo.com")
@allure.feature("Login")
@allure.story("Full Purchase Process")
@pytest.mark.usefixtures("driver")
class TestSauceDemo:

    @pytest.mark.smoke
    @allure.title("Процесс покупки товара на https://www.saucedemo.com/")
    @allure.severity(Severity.NORMAL)
    @allure.link(url="https://confluence.com", name="Documentation")
    def test_process_full(self):
        with allure.step("Open login page. Step 1"):
            self.driver.get("https://www.saucedemo.com/")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Login page",
                attachment_type=AttachmentType.PNG
            )

        with allure.step("Enter user credentials and login"):
            self.driver.find_element("xpath", "//input[@id='user-name']").clear()
            self.driver.find_element("xpath", "//input[@id='user-name']").send_keys("standard_user")
            self.driver.find_element("xpath", "//input[@id='password']").clear()
            self.driver.find_element("xpath", "//input[@id='password']").send_keys("secret_sauce")
            self.driver.find_element("xpath", "//input[@id='login-button']").click()
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="After login click",
                attachment_type=AttachmentType.PNG
            )

        with allure.step("Verify successful login.Step 2"):
            header = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(("xpath", "//span[@class='title']")))
            assert header.is_displayed(), "Login failed, header not visible"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Success authorization",
                attachment_type=AttachmentType.PNG
            )

        with allure.step("Checking successful login/password. Step 3"):
            assert self.driver.find_element("xpath", "//span[@class='title']").is_displayed()
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Success authorization",
                attachment_type=AttachmentType.PNG
            )


        with allure.step("Adding a product. Step 4"):
            self.driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']").click()
            self.driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
            self.driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
            cart_count = self.driver.find_element("class name", "shopping_cart_badge")
            assert cart_count.text == "3"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Success a product ",
                attachment_type=AttachmentType.PNG
            )

        with allure.step("Go to cart and proceed to checkout. Step 5"):
            self.driver.find_element("xpath", "//div[@id='shopping_cart_container']").click()
            header = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(("xpath", "//span[@class='title']")))
            assert header.text == "Your Cart"
            self.driver.find_element("xpath", "//button[@id='checkout']").click()
            header = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(("xpath", "//span[@class='title']")))
            assert header.text == "Checkout: Your Information"

            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Checkout page",
                attachment_type=AttachmentType.PNG
            )


        with allure.step("Product registration. Step 6"):
            self.driver.find_element("xpath", "//input[@id='first-name']").send_keys("Alexey")
            self.driver.find_element("xpath", "//input[@id='last-name']").send_keys("Egorushkov")
            self.driver.find_element("xpath", "//input[@id='postal-code']").send_keys("123456")
            self.driver.find_element("xpath", "//input[@id='continue']").click()
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Checkout product",
                attachment_type=AttachmentType.PNG
            )

        with allure.step("Finish purchases. Step 7"):
            self.driver.find_element("xpath", "//button[@id='finish']").click()
            header = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(("xpath", "//span[@class='title']")))
            assert header.text == "Checkout: Complete!"
            self.driver.find_element("xpath", "//button[@id='back-to-products']").click()
            header = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(("xpath", "//span[@class='title']")))
            assert header.text == "Products"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Finish product",
                attachment_type=AttachmentType.PNG
            )