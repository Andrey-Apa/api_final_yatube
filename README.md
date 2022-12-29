# Yatube API

## Описание

Проект Yatube API позволяет через простые запросы взаимодействовать с приложением Yatube для получение, ввода или изменения информации.

## Технологии
- Python 3.7.9
- Django 3.2.16
- Django REST Framework 3.12.4
- SimpleJWT 4.7.2
- Djoser 2.1.0
- Django filter 22.1
- Dotenv 0.21.0

## Запуск проекта
Клонировать репозиторий:
```bash
git clone git@github.com:Andrey-Apa/api_final_yatube.git
```
Cоздать и активировать виртуальное окружение(для Linux, MacOs - python3):
```bash
python -m venv venv
```
```bash
-для Windows
. venv/Scripts/activate
-для Linux, MacOs:
source env/bin/activate
```
Обновите pip
```bash
python -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```bash
pip install -r requirements.txt
```
Выполнить миграции:
```bash
cd yatube_api
```
```bash
python manage.py migrate
```
Запустить проект:
```bash
python manage.py runserver
```
Создайте суперпользователя:
```bash
python manage.py createsuperuser
```
Username (leave blank to use 'user'): # Придумайте логин (например, admin)
Email address: # укажите почту
Password: # придумайте пароль
Password (again): # повторите пароль

## Примеры запросов
- GET api/v1/posts/

Возвращает список всех постов.
```
[
    {
        "id": 1,
        "text": "string",
        "author": "string",
        "image": "string",
        "group": null,
        "pub_date": "2022-12-28T10:19:42.404733Z"
    },
]
```
- POST api/v1/posts/

Создаёт новый пост, в теле запроса можно передвать переменные "text": "string", "group": id, "image": "string"
(Только для авторизированных пользователей).
```
{
    "text": "string",
    "group": id,
    "image": "string"
}
```
Возвращает созданный пост, в поле автора указывается имя пользователя, отправившего запрос, доавляется дата публикации.
```
{
    "id": id,
    "text": "string",
    "author": "username",
    "image": "string",
    "group": id,
    "pub_date": "2022-12-29T08:37:05.620339Z"
}
```
- GET /api/v1/follow/

Возвращает список всех подписок пользователя(Только для авторизированных пользователей).
```
[
    {
        "user": "username",
        "following": "username"
    }
]
```
- POST /api/v1/follow/

Создает новую подписку на выбранного автора, в теле запроса необходимо указать "following": "username"
(Нельзя подписаться на автора дважды и на самого себя).
```
{
  "following": "username"
}
```
В случае удачной подписки возвращает юзернэйм подписчика и автора(на кого удалось подписаться).
```
{
        "user": "username",
        "following": "username"
    }
```
Более подробную информацию можно найти в "Документации"
## Документация к API

http://127.0.0.1:8000/redoc

## Автор

- Andrey Apashkin/Андрей Апашкин

## License

MIT

**Free Software, Not for commercial use!**