## Запуск backend'а
___


- `docker composer up -d` - поднять PostgreSQL с помощью Docker
- `poetry init` - установка зависимостей
- `poetry shell` - вход в виртуальное окружение
- `python src/manage.py migrate` - выполнить миграции
- `python src/manage.py runserver` - запуск сервера для разработки на http://localhost:8000
