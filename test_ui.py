import os
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

PAUSE_DURATION_SECONDS = 10


def driver_init():
    """Инициализация драйвера."""
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://rn.tektorg.ru/")
    driver.implicitly_wait(PAUSE_DURATION_SECONDS)
    return driver


def test_check_page(driver):
    """Поиск и проверка попадания на страницу "Проверка настроек ПК"."""
    try:
        text_menu = driver.find_element(By.XPATH, '//*[@id="ext-element-92"]')
        text_menu.click()
        driver.implicitly_wait(PAUSE_DURATION_SECONDS)
    except NoSuchElementException:
        print(f"{test_check_page.__doc__} - Элемент не найден!")


def test_title_page(driver):
    """Проверка титульника страницы."""
    try:
        title_text = driver.find_element(By.XPATH,
                                         '//*[@id="container-1069-innerCt"]')
        assert (
            title_text.get_attribute("innerHTML") == "Проверка настроек ПК"
        ), """Текст не соответствует требуемому!"""

    except NoSuchElementException:
        print(f"{test_title_page.__doc__} - Элемент не найден!")


def test_check_instructions(driver):
    """Инструкция по настройке ПК."""
    try:
        button = driver.find_element(By.XPATH,
                                     '//*[@id="button-1072-btnInnerEl"]')
        button.click()

    except NoSuchElementException:
        print(f"{test_check_instructions.__doc__} - Элемент не найден!")


def test_check_instructions_page(driver):
    """Проверка перехода на страницу "Электронная торговая площадка"."""
    if len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[1])
        wiki_tektorg = "https://wiki.tektorg.ru/"
        assert (
            driver.current_url == wiki_tektorg
        ), """Не перешел на страницу "Электронная торговая площадка"!"""
        driver.implicitly_wait(PAUSE_DURATION_SECONDS)
        driver.switch_to.window(driver.window_handles[0])


def test_check_download(driver):
    """Проверить загрузку файлов."""
    try:
        dowload_wnd = driver.find_element(
            By.XPATH, ' //*[@id="button-1078-btnInnerEl"]'
        )
        dowload_wnd.click()
        driver.implicitly_wait(PAUSE_DURATION_SECONDS)

        elm = driver.find_element(By.XPATH, "//input[@type='file']")
        elm.send_keys(os.getcwd() + "/image/1674386530_40372364.jpg")

        driver.implicitly_wait(PAUSE_DURATION_SECONDS)
        btn_download = driver.find_element(
            By.XPATH, '//*[@id="button-1110-btnInnerEl"]'
        )
        btn_download.click()

        btn_close = driver.find_element(By.XPATH, '//*[@id="button-1121"]')
        btn_close.click()

    except NoSuchElementException:
        print(f"{test_check_download.__doc__} - Элемент не найден!")


def test_check_settings(driver):
    """Проверить настройки ПК."""
    try:
        button = driver.find_element(By.XPATH,
                                     '//*[@id="button-1076-btnInnerEl"]')
        button.click()
        driver.implicitly_wait(PAUSE_DURATION_SECONDS)

        small_arrow = driver.find_element(By.XPATH,
                                          '//*[@id="ext-198-trigger-picker"]')
        small_arrow.click()
        driver.implicitly_wait(PAUSE_DURATION_SECONDS)

        cancel_button = driver.find_element(
            By.XPATH, '//*[@id="button-1093-btnInnerEl"]'
        )
        cancel_button.click()
        driver.implicitly_wait(PAUSE_DURATION_SECONDS)

    except NoSuchElementException:
        print(f"{test_check_settings.__doc__} - Элемент не найден!")


if __name__ == "__main__":
    driver = driver_init()
    test_check_page(driver)
    test_title_page(driver)
    test_check_instructions(driver)
    test_check_instructions_page(driver)
    test_check_settings(driver)
    test_check_download(driver)
