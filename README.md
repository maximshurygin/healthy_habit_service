# Проект атомных привычек

Проект является трекером полезных привычек.В нем реализована бэкенд-часть SPA веб-приложения.

## Используемые технологии

- Python
- Django
- Django REST Framework
- PostgreSQL
- Celery
- Redis

## Документация API

Документация доступна по ссылке:

- [http://127.0.0.1:8000/docs/](http://127.0.0.1:8000/docs/)

## CORS

Чтобы изменить настройки CORS, отредактируйте `settings.py`:

```
CORS_ALLOWED_ORIGINS = [
    "https://example-frontend.com",
    "https://another-frontend.com",
]
```

## Инструкция по развертыванию:

Склонировать репозиторий в IDE

В терминале введите команду:

```
git clone https://github.com/maximshurygin/coursework_7
```

Перейдите в папку проекта:

```
cd coursework_7
```

Соберите Docker образы:

```
docker-compose build
```

Запустите Docker Compose:

```
docker-compose up
```

Приложение будет доступно по адресу `http://localhost:8000/`

## Автор проекта:

Максим Шурыгин.

Если у вас возникли вопросы или проблемы при использовании проекта, свяжитесь со мной:
maximys2142@mail.ru

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
