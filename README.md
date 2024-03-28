
# Тестирование страницы "Проверка настроек ПК"
Тестирование UI выполнено с использованием Selenium WebDriver, инструмента для автоматизации действий веб-браузера.  

### Содержание
- [Тестирование страницы "Проверка настроек ПК"](#тестирование-страницы-проверка-настроек-пк)
    - [Содержание](#содержание)
    - [Реализованы возможности](#реализованы-возможности)
    - [Как запустить проект](#как-запустить-проект)
    - [Пример ошибки при тестировании](#пример-ошибки-при-тестировании)
    - [Пример успешного прохождения тестов](#пример-успешного-прохождения-тестов)
    - [Автор](#автор)


### Реализованы возможности
* Поиск и проверка попадания на страницу "Проверка настроек ПК".
* Проверка титульника страницы.
* Проверка "Инструкция по настройке ПК".
* Проверка перехода на страницу "Электронная торговая площадка".
* Проверить настройки ПК.
* Проверить загрузку файлов.


### Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Esperansa08/test_autotest.git
```
```
cd test_autotest
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```
```
Для Windows:
env/Scripts/activate

Для Linux или macos
source env/bin/activate
```
```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Запустить тест UI:
```
pytest
```

### Пример ошибки при тестировании
```
======================================================================= FAILURES ======================================================================= 
___________________________________________________________________ test_title_page ____________________________________________________________________ 

browser = <selenium.webdriver.chrome.webdriver.WebDriver (session="740bef11da404d40c7886078d91498b7")>

    def test_title_page(browser):
        """Проверка титульника страницы."""
        title_text = SearchHelper(browser)
        title = title_text.check_element_text()
>       assert title == "Проверка настроек ПК1"
E       AssertionError: assert 'Проверка настроек ПК' == 'Проверка настроек ПК1'
E
E         - Проверка настроек ПК1
E         ?                     -
E         + Проверка настроек ПК

test_ui.py:16: AssertionError
=============================================================== short test summary info ================================================================ 
FAILED test_ui.py::test_title_page - AssertionError: assert 'Проверка настроек ПК' == 'Проверка настроек ПК1'
```
### Пример успешного прохождения тестов
======================================================================== test session starts ===============================================================

platform win32 -- Python 3.11.3, pytest-8.1.1, pluggy-1.4.0 -- D:\Dev\test_autotest\venv\Scripts\python.exe
rootdir: D:\Dev\test_autotest
configfile: pytest.ini
testpaths: tests/
plugins: allure-pytest-2.13.3
collected 5 items                                                                                                                                                     

tests/test_ui.py::test_check_page
DevTools listening on ws://127.0.0.1:51211/devtools/browser/92d7d9b5-61fb-4153-bf2a-7f3a6797ec08
PASSED                                                                                                                       [ 20%]
tests/test_ui.py::test_title_page PASSED                                                                                                                       [ 40%] 
tests/test_ui.py::test_check_instructions PASSED                                                                                                               [ 60%] 
tests/test_ui.py::test_check_settings PASSED                                                                                                                   [ 80%] 
tests/test_ui.py::test_check_download [22952:24460:0328/214630.090:ERROR:device_event_log_impl.cc(195)] [21:46:30.089] USB: usb_service_win.cc:105 SetupDiGetDeviceProperty({{A45C254E-DF1C-4EFD-8020-67D146A850E0}, 6}) failed: ╨н╨╗╨╡╨╝╨╡╨╜╤В ╨╜╨╡ ╨╜╨░╨╣╨┤╨╡╨╜. (0x490)
PASSED                                                                                                                   [100%]

=================================================================== 5 passed, 1 warning in 16.04s =============================================================


### Автор
 * Савельева Анастасия 
 * [Почта](Visteria09@yandex.ru), [Github](https://github.com/Esperansa08) 
