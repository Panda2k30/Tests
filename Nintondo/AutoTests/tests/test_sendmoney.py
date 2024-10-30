import time
import allure
import pytest
from Nintondo.AutoTests.Pages.Registration_page import CreateMnemonic
from Nintondo.AutoTests.Data import Data
from Nintondo.AutoTests.Pages.Mane_page import ManePage
from .test_registration import test_restore_by_private_key

@allure.feature("Send money and verify balance")
@pytest.mark.usefixtures("driver")
def test_sendmoney(driver):
    # test_restore_by_private_key(driver) # Добавляем кошелек через приватный ключ
    test_restore_by_private_key = CreateMnemonic(driver)
    test_restore_by_private_key.enter_password(Data.PASS)  # Ввод пароля
    test_restore_by_private_key.conf_password(Data.CONFPASS)  # Подтверждение пароля
    test_restore_by_private_key.click_reg_button()  # Жмем на кнопку продолжения
    test_restore_by_private_key.type_reg_privacy_key()  # Выбираем восстановление через приватник
    test_restore_by_private_key.restore_input(Data.KEY_MONEY_WALLET)  # Вводим приватник
    test_restore_by_private_key.conf_create_wallet()  # Подтверждаем создание кошелька
    test_restore_by_private_key.choose_type_legacy()  # Выбираем:Legacy Type"
    test_restore_by_private_key.conf_recover_wallet()  # Подтверждаем создание кошелька
    test_sendmoney = ManePage(driver)
    test_sendmoney.get_balance()
    test_sendmoney.change_network()
    test_sendmoney.get_balance()