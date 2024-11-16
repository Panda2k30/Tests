# Stage 1: Clone and build the Chrome extension
FROM node:18 AS builder

# Set the working directory
WORKDIR /app

# Клонируем репозиторий
RUN git clone --branch dev https://github.com/Nintondo/extension.git .
RUN ls -l /app

# Install dependencies
RUN npm install -g bun && bun i

# Build the Chrome extension
RUN bun run test

RUN ls -la /app/dist

# Stage 2: Set up the main environment
FROM ubuntu:20.04

# Set an environment variable to suppress interactive requests
ENV DEBIAN_FRONTEND=noninteractive

# Upgrade the system and install the required dependencies
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

# Install Google Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -P /tmp && \
    dpkg -i /tmp/google-chrome-stable_current_amd64.deb || apt-get -f install -y && \
    rm /tmp/google-chrome-stable_current_amd64.deb

# Install Selenium, pytest and Allure pytest plugin
RUN pip3 install --upgrade pip
RUN pip3 install selenium pytest pytest-allure-adaptor

# Set the environment variable for PYTHONPATH
ENV PYTHONPATH=/usr/workspace/Nintondo

# Copy requirements.txt and install the dependencies
COPY requirements.txt /app/
WORKDIR /app
RUN pip3 install -r requirements.txt

# Copy the built extension from the builder stage
COPY --from=builder /app/dist/chrome /app/extension
RUN ls -l /app/extension

# Add browser paths to environment variables
ENV CHROMIUM_PATH="/usr/bin/chromium"
ENV GOOGLE_CHROME_BIN="/usr/bin/google-chrome-stable"

# Set the working directory for the tests
WORKDIR /usr/workspace/Nintondo/AutoTests/tests

# CMD updated to run tests with allure reporting
CMD ["pytest", "--alluredir=/app/allure-results", "-s"]
