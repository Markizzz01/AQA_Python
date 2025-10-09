class TestDemoQAAuth:

    def test_login_positive(self):
        self.driver.get("https://demoqa.com/login")

        # Заполняем форму логина
        self.driver.find_element("id", "userName").send_keys("testuser")
        self.driver.find_element("id", "password").send_keys("Abc123$!")
        self.driver.find_element("id", "login").click()

        # Проверяем наличие кнопки Logout
        logout_button = self.driver.find_element("id", "submit")
        assert logout_button.is_displayed(), "Логин не удался!"
