import pytest
from selenium import webdriver
from .Data import Data

@pytest.fixture(autouse=True, scope="function")
def driver(request):
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    # options.add_argument('--disable-extensions')
    extension_path = 'Nintodno/NintondoWallet.crx'
    options.add_extension(extension_path)

    # Инициализируем драйвер
    driver = webdriver.Chrome(options=options)
    driver.get(f'chrome-extension:{Data.EX_ID}/index.html')
    print("Драйвер инициализирован")  # Для отладки
    yield driver
    driver.quit()