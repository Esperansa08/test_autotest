from UIPages import SearchHelper


def test_check_page(browser):
    """Проверка попадания на страницу "Проверка настроек ПК"."""
    check_page = SearchHelper(browser)
    check_page.go_to_site()
    check_page.click_on_check_page()


def test_title_page(browser):
    """Проверка титульника страницы."""
    title_text = SearchHelper(browser)
    title = title_text.check_element_text()
    assert title == "Проверка настроек ПК"


def test_check_instructions(browser):
    """Инструкция по настройке ПК."""
    check_link = SearchHelper(browser)
    check_link.click_on_the_check_instructions()


def test_check_settings(browser):
    """Проверить настройки ПК."""
    set_link = SearchHelper(browser)
    set_link.click_on_the_check_settings()
    set_link.click_on_the_cancel_button()


def test_check_download(browser):
    """Проверить загрузку файлов."""
    check_download = SearchHelper(browser)
    check_download.click_on_the_dowload_wnd()
    check_download.click_on_the_dowload_elm()
    check_download.click_on_the_download_btn()
    check_download.click_on_the_btn_close()
