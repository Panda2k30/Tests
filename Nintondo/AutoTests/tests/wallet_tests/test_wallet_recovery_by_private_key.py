import time
import allure
import pytest
from Nintondo.AutoTests.pages.wallet.wallet_registration_page import CreateMnemonic
from Nintondo.AutoTests.data import Data
from Nintondo.AutoTests.pages.wallet.wallet_registration_page import LoginPageSelectors
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("driver")
@allure.feature("Restore wallet by private key")
# Проверяем восстановление кошелька приватником
def test_restore_by_private_key(driver):

    test_restore_by_private_key = CreateMnemonic(driver)

    test_restore_by_private_key.exec_id()
    test_restore_by_private_key.use_id()

    time.sleep(0.5)
    test_restore_by_private_key.enter_password(Data.PASS) # Ввод пароля
    test_restore_by_private_key.conf_password(Data.CONFPASS) # Подтверждение пароля
    test_restore_by_private_key.click_reg_button() # Жмем на кнопку продолжения
    test_restore_by_private_key.type_reg_privacy_key() # Выбираем восстановление через приватник
    test_restore_by_private_key.restore_input(Data.KEY_MONEY_WALLET) # Вводим приватник
    test_restore_by_private_key.conf_create_wallet() # Подтверждаем создание кошелька
    print("Выбираем тип кошелька: Native, по умолчанию")
    # Выбираем: Native по умолчанию"
    test_restore_by_private_key.conf_recover_wallet()  # Подтверждаем создание кошелька

@pytest.mark.usefixtures("driver")
@allure.feature("Restore wallet by invalid private key")
@pytest.mark.parametrize("data, expected_error", [
    ("", "Invalid private key"), #пустая строка
    (Data.INVALID_KEY_WALLET, "Invalid private key"), #невалидные данные
    ("-", "Invalid private key")]) #один символ
# Проверяем восстановление кошелька невалидным приватником
def test_restore_by_invalid_private_key(driver, data, expected_error):

    test_restore_by_invalid_private_key = CreateMnemonic(driver)

    test_restore_by_invalid_private_key.exec_id()
    test_restore_by_invalid_private_key.use_id()

    time.sleep(0.5)
    test_restore_by_invalid_private_key.enter_password(Data.PASS) # Ввод пароля
    test_restore_by_invalid_private_key.conf_password(Data.CONFPASS) # Подтверждение пароля
    test_restore_by_invalid_private_key.click_reg_button() # Жмем на кнопку продолжения
    test_restore_by_invalid_private_key.type_reg_privacy_key() # Выбираем восстановление через приватник
    test_restore_by_invalid_private_key.restore_input(data) # Вводим приватник
    test_restore_by_invalid_private_key.conf_create_wallet() # Подтверждаем создание кошелька
    print("Выбираем тип кошелька: Native, по умолчанию")
    # Выбираем: Native по умолчанию"
    test_restore_by_invalid_private_key.conf_recover_wallet()  # Подтверждаем создание кошелька

    try:
        # Ожидаем, что сообщение об ошибке станет видимым
        error_message = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "error"))
        )
        assert error_message.is_displayed(), "Сообщение об ошибке не отображается"
        assert error_message.text == expected_error, f"Ожидалось сообщение об ошибке: '{expected_error}', но получено: '{error_message.text}'"
    except Exception as e:
        pytest.fail(f"Ошибка при проверке сообщения: {e}")