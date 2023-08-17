# Project Title (django-orm-watching-storage)

Проект предназначен для отслеживания пребывания людей в здании и учета времени, проведенного ими внутри.

## Environment (Окружение)

- Python 3.6+

## Requirements (Зависимости)

Для установки всех зависимостей проекта выполните:
 
```
bash
pip install -r requirements.txt
```
`requirements.txt` должен содержать следующие библиотеки:
- requests
- psycopg2-binary
- environs

## Environment variables (Переменные окружения)

Для работы программы необходимо указать следующие переменные окружения:

- **DB_ENGINE**: 
  Драйвер базы данных, который вы используете. Например, `django.db.backends.postgresql_psycopg2`.

- **DB_HOST**: 
  Адрес хоста, на котором размещена ваша база данных.

- **DB_PORT**: 
  Порт, на котором ваша база данных принимает соединения.

- **DB_NAME**: 
  Название вашей базы данных.

- **DB_USER**: 
  Имя пользователя для доступа к базе данных.

- **DB_PASSWORD**: 
  Пароль для доступа к базе данных.

- **SECRET_KEY**: 
  Секретный ключ Django, используемый для обеспечения криптографической подписи.

- **DEBUG**: 
  Режим отладки Django. Если установлено значение `True`, будут показаны подробные отладочные сообщения.


## Run (Запуск)

Для запуска программы выполните следующую команду:
```
python manage.py runserver 0.0.0.0:8000
```
