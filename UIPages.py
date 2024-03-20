import os
from BaseApp import BasePage
from selenium.webdriver.common.by import By


class UiSeacrhLocators:
    # LOCATOR_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_CHECK_PAGE = (By.XPATH, '//*[@id="ext-element-92"]')
    LOCATOR_TITLE = (By.XPATH, '//*[@id="container-1069-innerCt"]')
    LOCATOR_NAVIGATION_BAR = (By.XPATH, ".service__name")
    LOCATOR_CHECK_INSTRUCTIONS = (By.XPATH,
                                  '//*[@id="button-1072-btnInnerEl"]')
    LOCATOR_CHECK_SETTINGS = (By.XPATH, '//*[@id="button-1076-btnInnerEl"]')
    LOCATOR_SET_CANCEL_BATTON = (By.XPATH, '//*[@id="button-1093-btnInnerEl"]')
    LOCATOR_DOWNLOAD_WND = (By.XPATH, ' //*[@id="button-1078-btnInnerEl"]')
    LOCATOR_INPUT_ELEMENT = (By.XPATH, "//input[@type='file']")
    LOCATOR_BUTTON_DOWNLOAD = (By.XPATH, '//*[@id="button-1110-btnInnerEl"]')
    LOCATOR_BUTTON_CLOSE = (By.XPATH, '//*[@id="button-1121"]')


class SearchHelper(BasePage):

    def click_on_check_page(self):
        return self.find_element(UiSeacrhLocators.LOCATOR_CHECK_PAGE,
                                 time=2).click()

    def check_element_text(self):
        return self.find_element(UiSeacrhLocators.LOCATOR_TITLE,
                                 time=2).get_attribute(
            "innerHTML"
        )

    def click_on_the_check_instructions(self):
        return self.find_element(
            UiSeacrhLocators.LOCATOR_CHECK_INSTRUCTIONS, time=2
        ).click()

    def click_on_the_check_settings(self):
        return self.find_element(
            UiSeacrhLocators.LOCATOR_CHECK_SETTINGS, time=10
        ).click()

    def click_on_the_cancel_button(self):
        return self.find_element(
            UiSeacrhLocators.LOCATOR_SET_CANCEL_BATTON, time=2
        ).click()

    def click_on_the_dowload_wnd(self):
        self.find_element(UiSeacrhLocators.LOCATOR_DOWNLOAD_WND,
                          time=2).click()

    def click_on_the_dowload_elm(self):
        elm = self.find_element(UiSeacrhLocators.LOCATOR_INPUT_ELEMENT,
                                time=10)
        elm.send_keys(os.getcwd() + "/image/1674386530_40372364.jpg")

    def click_on_the_download_btn(self):
        self.find_element(UiSeacrhLocators.LOCATOR_BUTTON_DOWNLOAD,
                          time=2).click()

    def click_on_the_btn_close(self):
        self.find_element(UiSeacrhLocators.LOCATOR_BUTTON_CLOSE,
                          time=2).click()
