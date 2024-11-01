import time
import allure
import pytest
from Nintondo.AutoTests.Pages.Registration_page import CreateMnemonic
from Nintondo.AutoTests.Data import Data
from Nintondo.AutoTests.Pages.Mane_page import ManePage
from Nintondo.AutoTests.Pages.Send_page import SendPage

@pytest.mark.usefixtures("driver")
@allure.feature("Send money and verify balance")

def test_sendmoney(driver):

    restore_by_private_key = CreateMnemonic(driver)
    sendmoney = SendPage(driver)
    change_network = ManePage(driver)

    restore_by_private_key.enter_password(Data.PASS)  # Ввод пароля
    restore_by_private_key.conf_password(Data.CONFPASS)  # Подтверждение пароля
    restore_by_private_key.click_reg_button()  # Жмем на кнопку продолжения

    restore_by_private_key.type_reg_privacy_key()  # Выбираем восстановление через приватник
    restore_by_private_key.restore_input(Data.KEY_MONEY_WALLET)  # Вводим приватник
    restore_by_private_key.conf_create_wallet()  # Подтверждаем создание кошелька
    restore_by_private_key.choose_type_legacy()  # Выбираем:Legacy Type"
    restore_by_private_key.conf_recover_wallet()  # Подтверждаем создание кошелька
    time.sleep(0.5)
    change_network.change_network()
    time.sleep(0.5)
    change_network.get_balance()
    change_network.send_page_btn()

    sendmoney.enter_address(Data.VALID_RECEIVE_ADDRESS)
    sendmoney.enter_amount(valid_amount=0.1)
    sendmoney.include_fee()
    sendmoney.save_address()
    sendmoney.cont_send_money()
    sendmoney.conf_send_money()
    sendmoney.back_to_home()
    time.sleep(0.5)
    change_network.get_balance()


