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

# Шаг 2: Создание и активация виртуального окружения

```sh
python -m venv venv
source venv/bin/activate
