import allure
import pytest
from time import sleep

# import requests
# from bs4 import BeautifulSoup
from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

PAUSE_DURATION_SECONDS = 5


def wait_of_element_located(xpath, driver):
    """ Функция ожидания элементов."""
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    return element


#@pytest.fixture
def driver_init():
    """ Инициализация драйвера."""
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://rn.tektorg.ru/")
    sleep(PAUSE_DURATION_SECONDS)
    return driver
    #driver.close()


@allure.title("Test Authentication")
def test_acc_page(driver):
    """ Поиск и проверка попадания на страницу "Аккредитация на ЭТП"."""
    try:
        title_text = wait_of_element_located('//*[@id="ext-element-97"]',
                                             driver)
        # title_text = wait_of_element_located('//*[@id="ext-element-92"]',
        #                                      driver)
        title_text.click()
    except NoSuchElementException:
        print(f"{test_acc_page.__doc__} - Элемент не найден!")
    sleep(PAUSE_DURATION_SECONDS)


def test_get_signature_page(driver):
    """ Проверка кнопки "Получить электронную подпись."""
    try:
        button_signature = wait_of_element_located(
            '//*[@id="button-1076-btnInnerEl"]', driver)
        button_signature.click()
    except NoSuchElementException:
        print(f"{test_get_signature_page.__doc__} - Элемент не найден!")
    sleep(PAUSE_DURATION_SECONDS)


def test_check_signature_page(driver):
    """ Проверка перехода на страницу e-signature."""
    if len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[1])
        e_signature = "https://service.tektorg.ru/e-signature"
        print(driver.current_url == e_signature)
        # если не совершен переход на страницу e_signature, то в терминале
        # выдается сообщение "Не перешел на страницу e-signature!""
        assert (
            driver.current_url == e_signature
        ), """Не перешел на страницу
        e-signature!"""
        sleep(PAUSE_DURATION_SECONDS)
        driver.switch_to.window(driver.window_handles[0])


def test_check_import_signature(driver):
    """ Проверка кнопки "Импортировать данные из электронной подписи"."""
    sleep(PAUSE_DURATION_SECONDS)
    try:
        time = driver.find_element(By.XPATH, '//*[@id="button-1080-btnInnerEl"]')
        print(time.title)
        time.click()
    except NoSuchElementException:
        print(f"{test_check_import_signature.__doc__} - Элемент не найден!")

# Действия с формами
# input_username.send_keys("standard_user")
# input_password.send_keys("secret_sauce")
# login_button.send_keys(Keys.RETURN)


if __name__ == "__main__":
    driver = driver_init()
    test_acc_page(driver)
    test_get_signature_page(driver)
    test_check_signature_page(driver)
    test_check_import_signature(driver)
