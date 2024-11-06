FROM python:3.12.0a4-alpine3.17

# Обновление репозиториев Alpine
RUN echo "https://dl-4.alpinelinux.org/alpine/v3.10/main" >> /etc/apk/repositories && \
    echo "https://dl-4.alpinelinux.org/alpine/v3.10/community" >> /etc/apk/repositories

# Установка Chromium и ChromeDriver
RUN apk update && \
    apk add --no-cache \
    chromium \
    chromium-chromedriver \
    nss \
    freetype \
    harfbuzz \
    ttf-freefont

# Установка зависимостей для работы с Selenium и тестами
RUN pip3 install selenium pytest webdriver-manager

# Get all the prereqs
# Добавляем публичный ключ для установки пакетов
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub

# Удаляем старый файл и скачиваем новый
RUN rm -f /tmp/glibc-2.30-r0.apk && \
    wget -O /tmp/glibc-2.30-r0.apk https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-2.30-r0.apk

# Проверка наличия файла перед скачиванием (удаление если существует)
RUN [ ! -f /tmp/glibc-2.30-r0.apk ] && \
    wget -O /tmp/glibc-2.30-r0.apk https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-2.30-r0.apk || echo "Файл уже существует"

# Дополнительный файл, скачиваем с другим именем
RUN wget -O /tmp/glibc-bin-2.30-r0.apk https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-bin-2.30-r0.apk

# Установка Allure
RUN apk add --no-cache openjdk11-jre curl tar && \
    curl -o allure-2.13.8.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.tgz && \
    tar -zxvf allure-2.13.8.tgz -C /opt/ && \
    rm -f /usr/bin/allure && \
    ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure && \
    rm allure-2.13.8.tgz

# Установка рабочего каталога
WORKDIR /usr/workspace

# Копирование зависимостей Python
COPY ./requirements.txt /usr/workspace

# Установка Python зависимостей
RUN pip3 install -r requirements.txt

# Указание пути к бинарнику Chromium для Selenium
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

# Открытие порта для Allure
EXPOSE 8080

# Команда по умолчанию для запуска тестов
CMD ["pytest"]