import time
import allure
import pytest
from Nintondo.AutoTests.Pages.Wallet_registration_page import CreateMnemonic
from Nintondo.AutoTests.data import Data
from Nintondo.AutoTests.Pages.Wallet_mane_page import ManePage
from Nintondo.AutoTests.Pages.Wallet_receive_Page import ReceivePage
from Nintondo.AutoTests.conftest import driver
import os

@pytest.mark.usefixtures("driver")
@allure.feature("Wallet address verification")
# Проверка адреса кошелька

def test_wallet_address_verification(driver):
    restore_by_private_key = CreateMnemonic(driver)
    check_address = ReceivePage(driver)
    test_wallet_address_verification = ManePage(driver)

    driver.get(f'chrome-extension:{Data.EX_ID}/index.html')

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
    test_wallet_address_verification.get_balance()
    test_wallet_address_verification.change_network()
    test_wallet_address_verification.receive_page_btn()
    # Получение адресов
    received_address = check_address.receive_address_btn()
    received_address_text = check_address.receive_address_text()

    screenshot_folder = 'screenshots'
    screenshot_file_path = os.path.join(screenshot_folder, 'screenshot-address.png')
    driver.get_screenshot_as_file(screenshot_file_path)
    print(f"Скриншот страницы с адресом сохранен в: {screenshot_file_path}")

    test_wallet_address_verification.back_btn()
    account_address = test_wallet_address_verification.account_address_btn()

    # Проверка на соответствие адресов в самом конце
    assert received_address == account_address, f"Ошибка: адреса не совпадают! Полученный адрес: '{received_address}', Ожидаемый адрес: '{account_address}'"
    assert received_address_text == account_address, f"Ошибка: адреса не совпадают! Полученный текст адреса: '{received_address_text}', Ожидаемый адрес: '{account_address}'"
