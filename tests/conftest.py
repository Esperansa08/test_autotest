import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

PAUSE_DURATION_SECONDS = 10


@pytest.fixture(scope="session")
def browser():
    """Инициализация драйвера."""
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(PAUSE_DURATION_SECONDS)
    yield driver
    driver.quit()
