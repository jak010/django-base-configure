# Django SandBox Template

- `Last Update`: 2025.06.20

# Table Of Contents

- [Purpose](#Purpose)
- [Enviornment](#Enviornment)
- [Structure](#Structure)

# Purpose

- 초기 django project를 template으로 만들고 가져다 쓰기

# Enviornment

- `Python` 3.11.5

# Structure

- SOURCE TREE
    ```text
    .
    ├── Makefile
    ├── readme.md
    ├── requirements.txt
    └── src
        ├── __init__.py
        ├── apps
        │   ├── __init__.py
        │   ├── admin.py
        │   ├── apps.py
        │   ├── migrations
        │   │   └── __init__.py
        │   ├── models
        │   │   ├── __init__.py
        │   │   └── sample.py
        │   ├── tests.py
        │   ├── urls.py
        │   └── views
        │       ├── __init__.py
        │       └── greeting.py
        ├── config
        │   ├── __init__.py
        │   ├── asgi.py
        │   ├── settings
        │   │   ├── __init__.py
        │   │   ├── base.py
        │   │   └── local.py
        │   ├── urls.py
        │   └── wsgi.py
        └── manage.py
    ```