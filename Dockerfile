FROM ubuntu:latest
LABEL authors="dev"

ENTRYPOINT ["top", "-b"]

# Используйте официальный образ Python
FROM python:3.10-slim

# Установите рабочую директорию
WORKDIR /app

# Скопируйте файлы зависимостей
COPY requirements.txt .

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Скопируйте весь код в контейнер
COPY Nintondo .

# Укажите команду для запуска тестов
CMD ["pytest"]