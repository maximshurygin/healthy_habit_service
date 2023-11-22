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

* Склонировать репозиторий в IDE

  В терминале ввести команду:

```
  git clone https://github.com/maximshurygin/coursework_7
```

Перейти в папку проекта:

```
    cd coursework_7
```

Создать и активировать виртуальное окружение:

```
    python3 -m venv venv
    source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
    pip install -r requirements.txt
```

Применить миграции:

```
    python manage.py migrate
```

Запустить сервер разработки:

```
    python manage.py runserver
```

Для работы с Celery и Redis запустить их в отдельных терминалах:

    Запуск Celery worker:

```
celery -A config worker -l info
```

    Запуск Celery beat:

```
celery -A config beat -l info
```

## Автор проекта:

Максим Шурыгин
Если у вас возникли вопросы или проблемы при использовании проекта, свяжитесь со мной:
maximys2142@mail.ru

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)