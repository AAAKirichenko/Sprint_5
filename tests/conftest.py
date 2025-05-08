import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    # Создаем опции для Chrome
    options = Options()
    options.add_argument("--window-size=1920,1080")  # Задаем размер окна
    # Инициализируем драйвер (путь к нему должен быть в PATH)
    driver = webdriver.Chrome(options=options)
    driver.get("https://stellarburgers.nomoreparties.site")
    yield driver
    driver.quit()


