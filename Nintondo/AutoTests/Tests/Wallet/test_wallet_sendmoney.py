import time
import allure
import pytest
from Nintondo.AutoTests.data import Data
from Nintondo.AutoTests.conftest import driver
from Nintondo.AutoTests.Pages.Wallet.wallet_registration_page import CreateMnemonic
from Nintondo.AutoTests.Pages.Wallet.wallet_mane_page import ManePage
from Nintondo.AutoTests.Pages.Wallet.wallet_send_page import SendPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("driver")
@allure.feature("Send money and verify balance")
# Проверяем отправку с валидным балансом
def test_valid_sendmoney(driver):

    # Функция для проверки отличий в TXID
    def are_txids_different(txid1, txid2):
        # Проверяем, отличаются ли TXID хотя бы одним символом
        return any(char1 != char2 for char1, char2 in zip(txid1, txid2)) or len(txid1) != len(txid2)

    restore_by_private_key = CreateMnemonic(driver)
    sendmoney = SendPage(driver)
    change_network = ManePage(driver)

    driver.get(f'chrome-extension:{Data.EX_ID}/index.html')

    time.sleep(0.5)
    # Ввод пароля и восстановление кошелька
    restore_by_private_key.enter_password(Data.PASS)
    restore_by_private_key.conf_password(Data.CONFPASS)
    restore_by_private_key.click_reg_button()

    restore_by_private_key.type_reg_privacy_key()
    restore_by_private_key.restore_input(Data.KEY_MONEY_WALLET)
    restore_by_private_key.conf_create_wallet()
    print("Выбираем тип кошелька: Native, по умолчанию")
    # Выбираем: Native по умолчанию"
    restore_by_private_key.conf_recover_wallet()

    time.sleep(0.5)
    change_network.get_balance()
    # Смена сети и получение старого баланса
    change_network.change_network()
    time.sleep(0.5)
    change_network.get_balance()

    # Получение старого TXID
    old_transaction_verify = change_network.verify_transaction()

    change_network.send_page_btn()

    # Отправка средств
    sendmoney.enter_address(Data.VALID_RECEIVE_ADDRESS)
    sendmoney.enter_amount(valid_amount=0.1)
    sendmoney.include_fee()
    sendmoney.save_address()
    sendmoney.cont_send_money()
    sendmoney.conf_send_money()
    sendmoney.back_to_home()
    time.sleep(0.5)

    # Получение нового баланса и TXID
    change_network.get_balance()
    new_transaction_verify = change_network.verify_transaction()

    # Проверка, что TXID изменился
    assert are_txids_different(new_transaction_verify, old_transaction_verify), (
        f"TXID не изменился! Старое значение: {old_transaction_verify}, "
        f"Новое значение: {new_transaction_verify}"
    )
    time.sleep(0.2)

@pytest.mark.usefixtures("driver")
@allure.feature("Sending money with an invalid balance")
@pytest.mark.parametrize("amount, blank, expected_error", [
    ("555555555", f"{Data.VALID_RECEIVE_ADDRESS}", "There's not enough money in your account"),
    ("", f"{Data.VALID_RECEIVE_ADDRESS}", "Minimum amount is 0.00000001 BEL"),
    ("0.1", "", "Insert receiver's address"),
    ("", "", "Insert receiver's address"),
    ("", f"{Data.NOT_VALID_ADDRESS}", "Invalid receiver's address")])

# Проверяем отправку с невалидным балансом и негативные сценарии
def test_invalid_sendmoney(driver, amount, blank, expected_error):

    restore_by_private_key = CreateMnemonic(driver)
    send_invalid_amount = SendPage(driver)
    change_network = ManePage(driver)

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
    restore_by_private_key.conf_recover_wallet() # Подтверждаем создание кошелька
    change_network.get_balance()
    change_network.change_network()
    time.sleep(0.5)
    change_network.get_balance()
    change_network.send_page_btn()

    send_invalid_amount.enter_address(blank)
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