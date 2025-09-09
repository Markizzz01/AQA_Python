# Ожидания в Selenium WebDriver: явные и неявные

# Импортируем необходимые модули
from selenium import webdriver  # для работы с браузером Chrome
from selenium.webdriver.chrome.service import Service  # для указания пути к драйверу
from selenium.webdriver.support.wait import WebDriverWait  # для явного ожидания
from webdriver_manager.chrome import ChromeDriverManager  # автоматически скачивает ChromeDriver
from selenium.webdriver.support import expected_conditions as EC  # ожидаемые условия (кликабельность, видимость и т.д.)

# Создаём объект опций для Chrome (можно добавлять настройки, например инкогнито)
options = webdriver.ChromeOptions()

# Настройка Service с указанием пути к драйверу, автоматически скачивается через ChromeDriverManager
service = Service(ChromeDriverManager().install())

# Создаём объект браузера Chrome с указанным Service и опциями
driver = webdriver.Chrome(service=service, options=options)

# Создаём объект явного ожидания: ждём до 10 секунд, проверяем условие каждую секунду
wait = WebDriverWait(driver, 10, poll_frequency=1)

# Открываем страницу demoqa с динамическими свойствами
driver.get("https://demoqa.com/dynamic-properties")

# Определяем локатор кнопки, которая появляется через 5 секунд
VISIBLE_BUTTON = ("id", "visibleAfter")  # кнопка имеет id="visibleAfter"

# Явное ожидание: ждём, пока кнопка станет кликабельной
wait.until(EC.element_to_be_clickable(VISIBLE_BUTTON))

# После того как кнопка стала кликабельной, кликаем на неё
driver.find_element(*VISIBLE_BUTTON).click()  # распаковываем кортеж через *, чтобы find_element его понял

# Закрываем браузер после выполнения действий
driver.quit()

