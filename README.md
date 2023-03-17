## Проект yamdb

### Описание

Проект YaMDb собирает отзывы (Review) пользователей на произведения (Title). Произведения делятся на категории (Category): книги, фильмы, музыка. Каждое произведение может получить несколько отзывов. Отзывы могут быть оставлены авторизованными пользователями, а администраторы могут модерировать отзывы.


### Технологии

Python 3.8.5, Django 3.2, Django REST Framework, Simple JWT,Git


### Установка

1. Клонируйте репозиторий на локальную машину
2. Создайте и активируйте виртуальное окружение
3. Установите зависимости из файла requirements.txt
4. Выполните миграции
5. Создайте суперпользователя
6. Запустите сервер
7. Перейдите по адресу http://127.0.0.1:8000/redoc/ для просмотра документации API

### Авторы

* **Акоб Джевагирян** - *Backend-разработчик* - [AkobArm]
* **Виктор Феоктистов** - *Backend-разработчик* - [Viktor-ux]
* **Данила Баранов** - *Backend-разработчик* - [Tesving]

### Клонирование БД

1. Перейти в Python shell командой python manage.py shell
2. Импорт необходимых модулей import os import csv
3. Установить путь до базы path = "с:/../api_yamdb/static/data"
4. Сделать импорт модели: from reviews.models import Genre, Category, Title, Review, Comment, GenreTitle from users.models import User
5. Последовательно для каждой модели запустить цикл записи данных:
на примере модели пользователей.
6. with open('users.csv') as csvfile: reader = csv.DictReader(csvfile) for row in reader: p = User(id=row['id'], username=row['username'], email=row['email'], role=row['role'], bio=row['bio'], first_name=row['first_name'], last_name=row['last_name']) p.save()
полный набор команд в файле import_db