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
@allure.feature("Valid Create wallet with new Mnemonic")
# Проверяем создание кошелька новым мнемоником
def test_valid_create_mnemonic(driver):

    test_create_mnemonic = CreateMnemonic(driver)

    test_create_mnemonic.exec_id()
    test_create_mnemonic.use_id()
    time.sleep(0.5)
    test_create_mnemonic.enter_password(Data.PASS) # Ввод пароля
    test_create_mnemonic.conf_password(Data.CONFPASS) # Подтверждение пароля
    test_create_mnemonic.click_reg_button() # Жмем на кнопку продолжения
    test_create_mnemonic.type_reg_new_mnem() # Выбираем тип авторизации: Новая мнемоника
    # test_create_mnemonic.copy_mnem() # Копируем фразы
    # test_create_mnemonic.paste_mnen() # Выводим фразы
    test_create_mnemonic.conf_save() # Подтверждаем сохранение мнемоники
    test_create_mnemonic.conf_create_wallet() # Подтверждаем создание кошелька
    print("Выбираем тип кошелька: Native, по умолчанию")
    # Выбираем: Native по умолчанию"
    test_create_mnemonic.conf_create_wallet() # Подтверждаем создание кошелька

@pytest.mark.usefixtures("driver")
@allure.feature("Invalid Create wallet with new Mnemonic")
# Проверяем невозможность создания кошелька, если пользователь не подтв. сохр. фраз
def test_invalid_create_mnemonic(driver):

    test_invalid_create_mnemonic = CreateMnemonic(driver)

    test_invalid_create_mnemonic.exec_id()
    test_invalid_create_mnemonic.use_id()
    time.sleep(0.5)
    test_invalid_create_mnemonic.enter_password(Data.PASS) # Ввод пароля
    test_invalid_create_mnemonic.conf_password(Data.CONFPASS) # Подтверждение пароля
    test_invalid_create_mnemonic.click_reg_button() # Жмем на кнопку продолжения
    test_invalid_create_mnemonic.type_reg_new_mnem() # Выбираем тип авторизации: Новая мнемоника

    createbtn_mnemonic = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(LoginPageSelectors.CREATE_BUTTON)
    )
    is_disabled_class = "disabled:cursor-not-allowed" in createbtn_mnemonic.get_attribute("class")

    assert is_disabled_class, "Ожидалось, что кнопка будет неактивной, но она доступна."
    print("- Кнопка действительно неактивна и имеет класс disabled:cursor-not-allowed")

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

@pytest.mark.usefixtures("driver")
@allure.feature("Restore wallet by valid mnemonic")
# Проверяем восстановление кошелька мнемоником
def test_restore_by_mnemonic(driver):

    test_restore_by_mnemonic = CreateMnemonic(driver)

    test_restore_by_mnemonic.exec_id()
    test_restore_by_mnemonic.use_id()

    time.sleep(0.5)
    test_restore_by_mnemonic.enter_password(Data.PASS)  # Ввод пароля
    test_restore_by_mnemonic.conf_password(Data.CONFPASS)  # Подтверждение пароля
    test_restore_by_mnemonic.click_reg_button()  # Жмем на кнопку продолжения
    test_restore_by_mnemonic.type_reg_mnemonic()  # Выбираем восстановление через мнемонику
    test_restore_by_mnemonic.type_reg_restore_mnem(Data.VALID_MNEMONIC_DATA)  # Вставляем мнемоники
    test_restore_by_mnemonic.click_restore_button()  # Жмем на кнопку продолжения
    test_restore_by_mnemonic.choose_type_native()   # Выбираем: Native Segwit
    test_restore_by_mnemonic.conf_create_wallet() # Подтверждаем создание кошелька

@pytest.mark.usefixtures("driver")
@allure.feature("Restore wallet by idvalid mnemonic")
@pytest.mark.parametrize("data, expected_error", [
    ("", "Please insert all the words"),
    (Data.INVALID_MNEMONIC_DATA , "Please insert all the words")])
# Проверяем негативные варианты создания мнемоника
def test_invalid_restore_by_mnemonic(driver, data, expected_error):

    test_invalid_restore_by_mnemonic = CreateMnemonic(driver)

    test_invalid_restore_by_mnemonic.exec_id()
    test_invalid_restore_by_mnemonic.use_id()

    time.sleep(0.5)
    test_invalid_restore_by_mnemonic.enter_password(Data.PASS)  # Ввод пароля
    test_invalid_restore_by_mnemonic.conf_password(Data.CONFPASS)  # Подтверждение пароля
    test_invalid_restore_by_mnemonic.click_reg_button()  # Жмем на кнопку продолжения
    test_invalid_restore_by_mnemonic.type_reg_mnemonic()  # Выбираем восстановление через мнемонику
    test_invalid_restore_by_mnemonic.type_reg_restore_mnem(data)  # Вставляем мнемоники
    test_invalid_restore_by_mnemonic.click_restore_button()  # Жмем на кнопку продолжения
    time.sleep(0.5)

    try:
        # Ожидаем, что сообщение об ошибке станет видимым
        error_message = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "error"))
        )
        assert error_message.is_displayed(), "Сообщение об ошибке не отображается"
        assert error_message.text == expected_error, f"Ожидалось сообщение об ошибке: '{expected_error}', но получено: '{error_message.text}'"
    except Exception as e:
        pytest.fail(f"Ошибка при проверке сообщения: {e}")