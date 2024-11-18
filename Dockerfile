# Stage 1: Clone and build the Chrome extension
FROM node:18 AS builder

WORKDIR /app

# Clone the extension repository
RUN git clone --branch dev https://github.com/Nintondo/extension.git .
RUN ls -l /app

# Install dependencies and build the extension
RUN npm install -g bun && bun i
RUN bun run test

RUN ls -la /app/dist

# Stage 2: Set up the main environment
FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget curl unzip gnupg2 ca-certificates lsb-release \
    libx11-dev libxcomposite1 libxrandr2 libglu1-mesa libnss3 \
    libgdk-pixbuf2.0-0 libatk-bridge2.0-0 libatk1.0-0 libgbm1 \
    libasound2 fonts-liberation xdg-utils libappindicator3-1 \
    libnspr4 libxtst6 sudo python3-pip python3-dev xclip x11-utils xvfb \
    libcups2 xfonts-100dpi xfonts-75dpi libxmu6 nodejs npm openjdk-11-jdk && \
    apt-get clean

RUN java -version

# Install Google Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -P /tmp && \
    dpkg -i /tmp/google-chrome-stable_current_amd64.deb || apt-get -f install -y && \
    rm /tmp/google-chrome-stable_current_amd64.deb

# Install Python dependencies
RUN pip3 install --upgrade pip
RUN pip3 install selenium pytest

# Install Allure CLI
RUN npm install -g allure-commandline --save-dev

ENV PATH="/usr/local/bin:${PATH}"

# Set PYTHONPATH
ENV PYTHONPATH=/usr/workspace/Nintondo

# Copy requirements and install them
COPY requirements.txt /app/
WORKDIR /app
RUN pip3 install -r requirements.txt

# Copy the built extension
COPY --from=builder /app/dist/chrome /app/extension
RUN ls -l /app/extension

# Create directories for Allure reports
USER root
RUN mkdir -p /app/allure-results /app/allure-report && chmod -R 777 /app/allure-results /app/allure-report

# Set proper ownership for allure directories
RUN chown -R root:root /app/allure-results /app/allure-report

# Add browser paths
ENV CHROMIUM_PATH="/usr/bin/chromium"
ENV GOOGLE_CHROME_BIN="/usr/bin/google-chrome-stable"

# Set JAVA_HOME
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=${JAVA_HOME}/bin:${PATH}

WORKDIR /usr/workspace/Nintondo/AutoTests/tests

# Ensure the tests and allure report generation runs correctly
CMD mkdir -p /app/allure-results /app/allure-report && \
    chmod -R 777 /app/allure-results /app/allure-report && \
    echo "Running tests..." && \
    pytest /usr/workspace/Nintondo/AutoTests/tests/mane_site_tests/test_connect.py --alluredir=/app/allure-results && \
    allure generate /app/allure-results --clean -o /app/allure-report