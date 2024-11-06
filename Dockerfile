# Используем образ Python с Alpine
FROM python:3.12.0a4-alpine3.17

# Добавляем репозитории для Alpine
RUN echo "https://dl-4.alpinelinux.org/alpine/v3.10/main" >> /etc/apk/repositories && \
    echo "https://dl-4.alpinelinux.org/alpine/v3.10/community" >> /etc/apk/repositories

# Устанавливаем зависимости для Chromium и chromedriver
RUN apk update && \
    apk add --no-cache \
    chromium \
    chromium-chromedriver \
    nss \
    freetype \
    harfbuzz \
    ttf-freefont \
    ca-certificates \
    && rm -rf /var/cache/apk/*

# Устанавливаем OpenJDK и Allure для отчетности
RUN apk add --no-cache openjdk11-jre curl tar && \
    curl -o allure-2.13.8.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.tgz && \
    tar -zxvf allure-2.13.8.tgz -C /opt/ && \
    ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure && \
    rm allure-2.13.8.tgz

# Устанавливаем glibc для совместимости с некоторыми зависимостями
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub && \
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-2.30-r0.apk && \
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-bin-2.30-r0.apk && \
    apk add --no-cache glibc-2.30-r0.apk glibc-bin-2.30-r0.apk && \
    rm glibc-2.30-r0.apk glibc-bin-2.30-r0.apk

# Копируем зависимости и устанавливаем их
WORKDIR /usr/workspace

# Установка Python зависимостей
COPY ./requirements.txt /usr/workspace/
RUN pip3 install --no-cache-dir -r requirements.txt

# Устанавливаем pytest
RUN pip install --no-cache-dir pytest

# Проверка установки pytest
RUN pytest --version

# Устанавливаем рабочую директорию
WORKDIR /usr/workspace/Nintondo

# Команда запуска тестов
CMD ["/bin/sh", "-c", "ls -la && pytest"]