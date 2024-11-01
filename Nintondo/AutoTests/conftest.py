import pytest
from selenium import webdriver
from .Data import Data

@pytest.fixture(autouse=True, scope="function")
def driver(request):
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    extension_path = "/home/dev/Autotests_wallet/Nintondo/NintondoWallet.crx"
    options.add_extension(extension_path)

    # Инициализируем драйвер
    driver = webdriver.Chrome(options=options)
    driver.get(f'chrome-extension:{Data.EX_ID}/index.html')
    driver.implicitly_wait(5)
    print("Драйвер инициализирован")  # Для отладки
    yield driver
    driver.quit()