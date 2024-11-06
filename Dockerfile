# Используем официальный образ Python на основе Ubuntu
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
    && apt-get clean

# Устанавливаем Google Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb || apt --fix-broken install -y

# Устанавливаем Chromium из репозитория Google
RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o /tmp/google-chrome-stable_current_amd64.deb \
    && dpkg -i /tmp/google-chrome-stable_current_amd64.deb \
    && apt-get update && apt-get install -f -y

RUN apt-get update && apt-get install -y xclip
RUN apt-get update && apt-get install -y x11-utils
RUN apk add --no-cache xvfb-run
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
CMD ["pytest", "AutoTests/Tests/wallet_tests/test_wallet_sendmoney.py"]
