
# Тестирование страницы АО "ТЭК-Торг" Аккредитация нового пользователя на ЭТП

### Содержание:
- [Тестирование страницы АО "ТЭК-Торг" Аккредитация нового пользователя на ЭТП](#тестирование-страницы-ао-тэк-торг-аккредитация-нового-пользователя-на-этп)
    - [Содержание:](#содержание)
    - [Реализованы возможности](#реализованы-возможности)
    - [Как запустить проект:](#как-запустить-проект)
    - [Примеры запросов](#примеры-запросов)
      - [Публикация и получение категорий](#публикация-и-получение-категорий)
      - [Частичное обновление и получение произведений](#частичное-обновление-и-получение-произведений)
      - [Публикация и удаление комментария](#публикация-и-удаление-комментария)
    - [Автор:](#автор)


### Реализованы возможности
* Поиск и проверка попадания на страницу "Аккредитация на ЭТП".
* Проверка кнопки "Получить электронную подпись.
* Проверка перехода на страницу e-signature.
* 
* Получение, создание, обновление, удаление отзывов.
* Получение, создание, обновление, удаление комментариев к отзыву.
* Получение, создание, обновление, удаление пользователей.
* Регистрация пользователей и выдача токенов


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Esperansa08/api_yamdb.git
```
```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```
```
Для Windows:
env/Scripts/activate

Для Linux или macos
source env/bin/activate
```
```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```

Выполнить миграции:
```
python3 manage.py migrate
```

Запустить проект:
```
python3 manage.py runserver
```


### Примеры запросов

#### Публикация и получение категорий

Request: [GET] http://127.0.0.1:8000/api/v1/categories/

Response:
```
{
  "count": 0,
  "next": "string",
  "previous": "string",
  "results": [
    {
      "name": "string",
      "slug": "string"
    }
  ]
}
```
Request: [POST] http://127.0.0.1:8000/api/v1/categories/

Response:
```
{
  "name": "string",
  "slug": "string"
}
```

#### Частичное обновление и получение произведений
Request: [GET] http://127.0.0.1:8000/api/v1/titles/

Response:
```
{
  "count": 0,
  "next": "string",
  "previous": "string",
  "results": [
    {
      "id": 0,
      "name": "string",
      "year": 0,
      "rating": 0,
      "description": "string",
      "genre": [
        {
          "name": "string",
          "slug": "string"
        }
      ],
      "category": {
        "name": "string",
        "slug": "string"
      }
    }
  ]
}
```
Request: [PATCH] http://127.0.0.1:8000/api/v1/titles/{titles_id}/

Response:
```
{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}
```

#### Публикация и удаление комментария

Request: [POST] http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/

Response:
```
{
  "text": "string"
}
```
Request: [DELETE] http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/



### Автор:
 * Савельева Анастасия (Visteria09@yandex.ru, https://github.com/Esperansa08)
