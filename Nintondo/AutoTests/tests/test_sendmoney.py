import time
import allure
import pytest
from Nintondo.AutoTests.Pages.Registration_page import CreateMnemonic
from Nintondo.AutoTests.Data import Data
from Nintondo.AutoTests.Pages.Mane_page import ManePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Nintondo.AutoTests.Pages.Send_page import SendPage
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("driver")
@allure.feature("Send money and verify balance")

def test_valid_sendmoney(driver):

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
    old_balance = change_network.get_balance()
    change_network.send_page_btn()

    sendmoney.enter_address(Data.VALID_RECEIVE_ADDRESS)
    sendmoney.enter_amount(valid_amount=0.1)
    sendmoney.include_fee()
    sendmoney.save_address()
    sendmoney.cont_send_money()
    sendmoney.conf_send_money()
    sendmoney.back_to_home()
    time.sleep(0.5)
    new_balance = change_network.get_balance()

    # Проверка уменьшения баланса после перевода
    assert old_balance > new_balance, (
        f"Ошибка: баланс не уменьшился после перевода. "
        f"Начальный баланс: {old_balance}, новый баланс: {new_balance}"
    )

    time.sleep(0.2)


@pytest.mark.usefixtures("driver")
@allure.feature("Sending money with an invalid balance")
@pytest.mark.parametrize("amount, expected_error", [
    ("555555555", "There's not enough money in your account")])

def test_invalid_sendmoney(driver, amount, expected_error):

    restore_by_private_key = CreateMnemonic(driver)
    send_invalid_amount = SendPage(driver)
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
    change_network.get_balance()
    change_network.send_page_btn()

    send_invalid_amount.enter_address(Data.VALID_RECEIVE_ADDRESS)
    send_invalid_amount.enter_amount(amount)
    send_invalid_amount.cont_send_money()

    try:
        error_message = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "error"))
        )
        assert error_message.is_displayed(), "Сообщение об ошибке не отображается"
        assert error_message.text == expected_error, f"Ожидалось сообщение об ошибке: '{expected_error}', но получено: '{error_message.text}'"
    except Exception as e:
        pytest.fail(f"Ошибка при проверке сообщения: {e}")