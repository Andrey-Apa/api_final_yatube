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

python manage.py migrate
```
Запустить проект:
```bash
python manage.py runserver
```

## Документация к API

http://127.0.0.1:8000/redoc

## Автор

- Andrey Apashkin/Андрей Апашкин

## License

MIT

**Free Software, Not for commercial use!**