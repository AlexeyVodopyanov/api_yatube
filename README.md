# CRUD для Yatube

<h1 align="center">Привет всем! Меня зовут <a href="https://daniilshat.ru/" target="_blank">Алексей</a> 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>

## Описание проекта

CRUD для Yatube.

API доступен только аутентифицированным пользователям. Аутентификация реализована по токену TokenAuthentication. Аутентифицированный пользователь авторизован на изменение и удаление своего контента, в остальных случаях доступ предоставляется только для чтения.

## Функционал

- Реализован REST API для сервиса публикации постов, Yatube;
- Аутентификация по JWT-токену;
- Работает со всеми модулями Yatube: постами, комментариями, группами и подписчиками.
- Поддерживает методы GET, POST, PUT, PATCH, DELETE;
- Предоставляет данные в формате JSON.

## Инструкции по развертке

# Шаг 1: Клонирование репозитория

```sh
git clone https://github.com/yourusername/api_yatube.git
cd api_yatube
```

# Шаг 2: Создание и активация виртуального окружения

```sh
python -m venv venv
source venv/bin/activate
```

# Шаг 3: Установка зависимостей

```sh
python -m pip install --upgrade pip
pip install -r requirements.txt
```

# Шаг 4: Применение миграций

```sh
cd yatube
python manage.py makemigrations
python manage.py migrate
```

# Шаг 5: Запуск сервера

```sh
python manage.py runserver
```

## Аутентификация

# Получение токена

```sh
{
    "username": "yourusername",
    "password": "yourpassword"
}
```

# Примеры запросов и ответов

Результат POST-запроса с токеном пользователя на добавление нового поста:

1. Пример запроса:

```sh
{
    "text": "Текст",
    "group": 1
}
```

2. Пример ответа:

```sh
{
    "id": 1,
    "text": "Текст",
    "author": "username",
    "image": null,
    "group": 1,
    "pub_date": "2024-07-04T20:47:10.084572Z"
}
```

## Информация об авторе

Проект разработан Алексей в рамках обучения и практики разработки REST API с использованием Django и Django Rest Framework.

Готов мой первый проект в Яндекс.Практикум! Этот проект — практическая реализация моих знаний и опыта.

## Технологии

- VSCode
- PyChram
- Python
- Django
- DRF
- Postman

<a href="https://www.python.org/" rel="nofollow"><img src="https://camo.githubusercontent.com/7d0627d59935971a0446fd5eaa2553e52229fae3cd3e5d54ee04fe99dbe77fc8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d507974686f6e2d3436343634313f7374796c653d666c61742d737175617265266c6f676f3d507974686f6e" alt="Python" data-canonical-src="https://img.shields.io/badge/-Python-464641?style=flat-square&amp;logo=Python" style="max-width: 100%;"></a>
<a href="https://www.djangoproject.com/" rel="nofollow"><img src="https://camo.githubusercontent.com/d21a711f33659c80dec71f941b45c19151312a4ef9552adef6c0475b27a28fb5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446a616e676f2d3436343634363f7374796c653d666c61742d737175617265266c6f676f3d646a616e676f" alt="Django" data-canonical-src="https://img.shields.io/badge/Django-464646?style=flat-square&amp;logo=django" style="max-width: 100%;"></a>
<a href="https://docs.pytest.org/en/6.2.x/" rel="nofollow"><img src="https://camo.githubusercontent.com/8d89a23df24367872457843f8866a43174f9247e921fc812b45d3a34ec88f49a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5079746573742d3436343634363f7374796c653d666c61742d737175617265266c6f676f3d707974657374" alt="Pytest" data-canonical-src="https://img.shields.io/badge/Pytest-464646?style=flat-square&amp;logo=pytest" style="max-width: 100%;"></a>
<a href="https://www.postman.com/" rel="nofollow"><img src="https://camo.githubusercontent.com/10feee2f301abe7389f4712e5ee41b7d0776eb3fd969642cfd3bef30ed711de5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f506f73746d616e2d3436343634363f7374796c653d666c61742d737175617265266c6f676f3d706f73746d616e" alt="Postman" data-canonical-src="https://img.shields.io/badge/Postman-464646?style=flat-square&amp;logo=postman" style="max-width: 100%;"></a>
