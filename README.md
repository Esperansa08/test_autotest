
# Тестирование страницы АО "ТЭК-Торг" Аккредитация нового пользователя на ЭТП

### Содержание:
- [Тестирование страницы АО "ТЭК-Торг" Аккредитация нового пользователя на ЭТП](#тестирование-страницы-ао-тэк-торг-аккредитация-нового-пользователя-на-этп)
    - [Содержание:](#содержание)
    - [Реализованы возможности](#реализованы-возможности)
    - [Как запустить проект:](#как-запустить-проект)
    - [Автор:](#автор)


### Реализованы возможности
* Поиск и проверка попадания на страницу "Аккредитация на ЭТП".
* Проверка кнопки "Получить электронную подпись.
* Проверка перехода на страницу e-signature.
* 



### Как запустить проект:

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
python test_ui.py
```


### Автор:
 * Савельева Анастасия (Visteria09@yandex.ru, https://github.com/Esperansa08)
