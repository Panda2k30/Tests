# Используем официальный образ Python на основе Ubuntu
FROM ubuntu:20.04

# Устанавливаем переменную окружения для подавления интерактивных запросов
ENV DEBIAN_FRONTEND=noninteractive

# Переходим на пользователя root для установки пакетов с максимальными правами
USER root

# Обновляем систему и устанавливаем необходимые зависимости
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    gnupg2 \
    ca-certificates \
    lsb-release \
    libx11-dev \
    libxcomposite1 \
    libxrandr2 \
    libglu1-mesa \
    libnss3 \
    libgdk-pixbuf2.0-0 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libgbm1 \
    libasound2 \
    fonts-liberation \
    xdg-utils \
    libappindicator3-1 \
    libnspr4 \
    libxtst6 \
    sudo \
    python3-pip \
    python3-dev \
    xclip \
    x11-utils \
    xvfb \
    libcups2 \
    xfonts-100dpi \
    xfonts-75dpi \
    libxmu6 \
    && apt-get clean  # Очищаем кэш apt, чтобы уменьшить размер образа

# Устанавливаем Google Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb || apt --fix-broken install -y

# Устанавливаем Chromium из репозитория Google
RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o /tmp/google-chrome-stable_current_amd64.deb \
    && dpkg -i /tmp/google-chrome-stable_current_amd64.deb \
    && apt-get update && apt-get install -f -y

# Устанавливаем Selenium и pytest
RUN pip3 install --upgrade pip
RUN pip3 install selenium pytest

# Копируем requirements.txt в контейнер
COPY requirements.txt /app/

WORKDIR /app
RUN pip3 install -r requirements.txt

# Добавляем пути к браузерам в переменные среды
ENV CHROMIUM_PATH="/usr/bin/chromium"
ENV GOOGLE_CHROME_BIN="/usr/bin/google-chrome-stable"

# Запускаем pytest для тестов
CMD ["pytest"]
