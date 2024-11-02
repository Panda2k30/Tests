import pytest
from selenium import webdriver
import os
from .Data import Data
import allure

@pytest.fixture(autouse=True, scope="function")
def driver(request):
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("--window-size=1280,720")
    extension_path = "/home/alexsey/Tests/Nintondo/NintondoWallet.crx"
    options.add_extension(extension_path)

    # Инициализируем драйвер
    driver = webdriver.Chrome(options=options)
    driver.get(f'chrome-extension:{Data.EX_ID}/index.html')
    driver.implicitly_wait(4)
    print("Драйвер инициализирован")  # Для отладки

    screenshot_dir = "screenshots"
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    yield driver

    screenshot_path = f"{screenshot_dir}/{request.node.name}.png"
    driver.save_screenshot(screenshot_path)

    allure.attach.file(screenshot_path, name="Screenshot", attachment_type=allure.attachment_type.PNG)

    driver.quit()