import os
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchWindowException
import allure

@pytest.fixture(autouse=True, scope="function")
def driver(request):
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("--window-size=1280,720")
    extension_path = "/home/dev/Autotests_wallet/Nintondo/NintondoWallet.crx"
    options.add_extension(extension_path)

    # Инициализируем драйвер
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(4)
    print("Драйвер инициализирован")  # Для отладки

    # Директория для скриншотов
    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)

    yield driver

    # Пробуем создать скриншот для алюра
    screenshot_path = f"{screenshot_dir}/{request.node.name}.png"
    try:
        if len(driver.window_handles) > 0:
            driver.save_screenshot(screenshot_path)
            allure.attach.file(screenshot_path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
        else:
            print("Скриншот не сделан, так как все окна были закрыты")
    except NoSuchWindowException:
        print("Окно было закрыто, скриншот не сделан")
    finally:
        driver.quit()