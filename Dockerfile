# Stage 1: Clone and build the Chrome extension
FROM node:18 AS builder

# Устанавливаем рабочую директорию
WORKDIR /app

# Клонируем репозиторий
RUN git clone https://github.com/Nintondo/extension.git .

# Устанавливаем зависимости
RUN npm install -g bun && bun i

# Собираем Chrome-расширение
RUN bun chrome

# Stage 2: Set up the main environment
FROM ubuntu:20.04

# Устанавливаем переменную окружения для подавления интерактивных запросов
ENV DEBIAN_FRONTEND=noninteractive

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
    && apt-get clean

# Устанавливаем Google Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -P /tmp && \
    dpkg -i /tmp/google-chrome-stable_current_amd64.deb || apt-get -f install -y && \
    rm /tmp/google-chrome-stable_current_amd64.deb

# Устанавливаем Selenium и pytest
RUN pip3 install --upgrade pip
RUN pip3 install selenium pytest

# Копируем requirements.txt и устанавливаем зависимости
COPY requirements.txt /app/
WORKDIR /app
RUN pip3 install -r requirements.txt

# Копируем собранное расширение из builder стадии
COPY --from=builder /app/dist/chrome /app/extension

# Добавляем пути к браузерам в переменные среды
ENV GOOGLE_CHROME_BIN="/usr/bin/google-chrome-stable"

# Запускаем pytest для тестов
CMD ["pytest"]
