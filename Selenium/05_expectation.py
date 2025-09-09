# Ожидания в Selenium WebDriver: явные и неявные

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка опций Chrome
options = webdriver.ChromeOptions()  # Создаём объект опций
# options.add_argument("--incognito")  # пример дополнительной настройки

# Импорт и настройка драйвера через Service и менеджер ChromeDriver
service = Service(ChromeDriverManager().install())  # Автоматически скачивает и указывает путь к драйверу
driver = webdriver.Chrome(service=service, options=options)  # Создаём объект Chrome с указанным драйвером и настройками

# Создаём объект явного ожидания
wait = WebDriverWait(driver, 30, poll_frequency=1)  # Ждём до 30 секунд, проверяем условие каждую секунду

# Открываем страницу для теста
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")  # Загружаем тестовый сайт

# Определяем локатор кнопки для добавления элемента
ADD_ELEMENT_BUTTON = ("xpath", "//button[text()='Add Element']")  # Кортеж с типом локатора и значением

# Явное ожидание: ждём, пока кнопка станет кликабельной
wait.until(EC.element_to_be_clickable(ADD_ELEMENT_BUTTON))  # Ждём кликабельность кнопки, без распаковки кортежа

# После того как кнопка стала кликабельной, кликаем на неё
driver.find_element(*ADD_ELEMENT_BUTTON).click()  # Распаковываем кортеж через * и выполняем клик