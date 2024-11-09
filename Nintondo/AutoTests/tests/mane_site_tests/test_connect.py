import time
import allure
import pytest
from Nintondo.AutoTests.pages.wallet.wallet_registration_page import CreateMnemonic
from Nintondo.AutoTests.data import Data
from Nintondo.AutoTests.pages.mane_site.nintondo_mane import NintondoPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Nintondo.AutoTests.conftest import driver
from Nintondo.AutoTests.pages.wallet.wallet_mane_page import ManePage

@pytest.mark.usefixtures("driver")
@allure.feature("Test Connect wallet_tests")
# Подключаем кошелек к mane_site
def test_connect(driver):

    restore_by_private_key = CreateMnemonic(driver)
    connect = NintondoPage(driver)
    change_network = ManePage(driver)

    ex_id = restore_by_private_key.exec_id()
    restore_by_private_key.use_id()

    time.sleep(0.5)
    restore_by_private_key.enter_password(Data.PASS)  # Ввод пароля
    restore_by_private_key.conf_password(Data.CONFPASS)  # Подтверждение пароля
    restore_by_private_key.click_reg_button()  # Жмем на кнопку продолжения

    restore_by_private_key.type_reg_privacy_key()  # Выбираем восстановление через приватник
    restore_by_private_key.restore_input(Data.KEY_MONEY_WALLET)  # Вводим приватник
    restore_by_private_key.conf_create_wallet()  # Подтверждаем создание кошелька
    print("Выбираем тип кошелька: Native, по умолчанию")
    # Выбираем: Native по умолчанию"
    restore_by_private_key.conf_recover_wallet()  # Подтверждаем создание кошелька

    change_network.get_balance()
    change_network.change_network(ex_id)

    driver.get("https://nintondo.io/")

    time.sleep(0.3)
    connect.change_network_btn()

    driver.set_window_size(800, 768)

    time.sleep(0.3)
    connect.connect_btn()

    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    windows = driver.window_handles
    time.sleep(0.3)
    driver.switch_to.window(windows[1])
    print(driver.title)

    connect.sign_btn()
    time.sleep(0.2)
    driver.switch_to.window(windows[0])
    driver.set_window_size(1280, 720)