# API для YaMDb
![workflow](https://github.com/awrora2/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

API для блога, который позволяет оставлять отзывы на произведения, на основе которых составляется его общий рейтинг. 

## Getting Started:
Клонировать репозиторий и перейти в него в командной строке:
```
https://github.com/awrora2/infra_sp2.git
```
Установить и активировать виртуальное окружение:
```
docker-compose up -d --build
```
Выполнить миграции, создать суперпользователя и собрать статику:
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```
В папке с файлом manage.py выполнить команду:
```
docker-compose up
```
Приложение доступно по адресу:
```
http://localhost
```
В файле находятся переменные окружения такие, как:
```
DB_NAME,
POSTGRES_USER,
POSTGRES_PASSWORD,
DB_HOST,
DB_PORT.
```


## Prerequisites:
```
requests==2.26.0
asgiref==3.2.10
django==2.2.16
django-filter==2.4.0
djangorestframework==3.12.4
djangorestframework-simplejwt==4.8.0
gunicorn==20.0.4
psycopg2-binary==2.8.6
PyJWT==2.1.0
pytest==6.2.4
pytest-django==4.4.0
pytest-pythonpath==0.7.3
pytz==2020.1
sqlparse==0.3.1
python-dotenv==0.20.0
```

### Examples:

В рамках API YaMDb реализованы следующие ресурсы:
- аутентификация;
- отзывы на произведения;
- комментарии к отзывам.

Документация доступна после запуска по адресу:
```
http://127.0.0.1/redoc/
```

