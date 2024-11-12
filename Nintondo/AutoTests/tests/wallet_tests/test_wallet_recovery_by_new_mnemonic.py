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

def test_valid_create_mnemonic(driver):

    test_create_mnemonic = CreateMnemonic(driver)

    test_create_mnemonic.exec_id()
    test_create_mnemonic.use_id()
    time.sleep(0.5)
    test_create_mnemonic.enter_password(Data.PASS) # Enter password
    test_create_mnemonic.conf_password(Data.CONFPASS) # Confirm password
    test_create_mnemonic.click_reg_button() # Hit the continue button
    test_create_mnemonic.type_reg_new_mnem() # Select authorization type: New mnemonic
    # test_create_mnemonic.copy_mnem() # Копируем фразы
    # test_create_mnemonic.paste_mnen() # Выводим фразы
    test_create_mnemonic.conf_save() # Confirm that the mnemonic has been saved
    test_create_mnemonic.conf_create_wallet() # Confirm wallet creation
    print("// Choose wallet type: Native, by default //")
    test_create_mnemonic.conf_create_wallet() # Confirm wallet creation

@pytest.mark.usefixtures("driver")
@allure.feature("Invalid Create wallet with new Mnemonic")

def test_invalid_create_mnemonic(driver):

    test_invalid_create_mnemonic = CreateMnemonic(driver)

    test_invalid_create_mnemonic.exec_id()
    test_invalid_create_mnemonic.use_id()
    time.sleep(0.5)
    test_invalid_create_mnemonic.enter_password(Data.PASS)
    test_invalid_create_mnemonic.conf_password(Data.CONFPASS)
    test_invalid_create_mnemonic.click_reg_button()
    test_invalid_create_mnemonic.type_reg_new_mnem()

    createbtn_mnemonic = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(LoginPageSelectors.CREATE_BUTTON)
    )
    is_disabled_class = "disabled:cursor-not-allowed" in createbtn_mnemonic.get_attribute("class")

    assert is_disabled_class, "Ожидалось, что кнопка будет неактивной, но она доступна."
    print("- Кнопка действительно неактивна и имеет класс disabled:cursor-not-allowed")

@pytest.mark.usefixtures("driver")
@allure.feature("Restore wallet by private key")

def test_restore_by_private_key(driver):

    test_restore_by_private_key = CreateMnemonic(driver)

    test_restore_by_private_key.exec_id()
    test_restore_by_private_key.use_id()

    time.sleep(0.5)
    test_restore_by_private_key.enter_password(Data.PASS)
    test_restore_by_private_key.conf_password(Data.CONFPASS)
    test_restore_by_private_key.click_reg_button()
    test_restore_by_private_key.type_reg_privacy_key()
    test_restore_by_private_key.restore_input(Data.KEY_MONEY_WALLET)
    test_restore_by_private_key.conf_create_wallet()
    print("// Choose wallet type: Native, by default //")
    test_restore_by_private_key.conf_recover_wallet()

@pytest.mark.usefixtures("driver")
@allure.feature("Restore wallet by invalid private key")
@pytest.mark.parametrize("data, expected_error", [
    ("", "Invalid private key"),
    (Data.INVALID_KEY_WALLET, "Invalid private key"),
    ("-", "Invalid private key")])

def test_restore_by_invalid_private_key(driver, data, expected_error):

    test_restore_by_invalid_private_key = CreateMnemonic(driver)

    test_restore_by_invalid_private_key.exec_id()
    test_restore_by_invalid_private_key.use_id()

    time.sleep(0.5)
    test_restore_by_invalid_private_key.enter_password(Data.PASS)
    test_restore_by_invalid_private_key.conf_password(Data.CONFPASS)
    test_restore_by_invalid_private_key.click_reg_button()
    test_restore_by_invalid_private_key.type_reg_privacy_key()
    test_restore_by_invalid_private_key.restore_input(data)
    test_restore_by_invalid_private_key.conf_create_wallet()
    print("// Choose wallet type: Native, by default //")
    test_restore_by_invalid_private_key.conf_recover_wallet()

    try:
        error_message = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "error"))
        )
        assert error_message.is_displayed(), "The error message is not displayed"
        assert error_message.text == expected_error, f"An error message was expected: '{expected_error}', but received: '{error_message.text}'"
    except Exception as e:
        pytest.fail(f"Message validation error: {e}")

@pytest.mark.usefixtures("driver")
@allure.feature("Restore wallet by valid mnemonic")

def test_restore_by_mnemonic(driver):

    test_restore_by_mnemonic = CreateMnemonic(driver)

    test_restore_by_mnemonic.exec_id()
    test_restore_by_mnemonic.use_id()

    time.sleep(0.5)
    test_restore_by_mnemonic.enter_password(Data.PASS)
    test_restore_by_mnemonic.conf_password(Data.CONFPASS)
    test_restore_by_mnemonic.click_reg_button()
    test_restore_by_mnemonic.type_reg_mnemonic()
    test_restore_by_mnemonic.type_reg_restore_mnem(Data.VALID_MNEMONIC_DATA)
    test_restore_by_mnemonic.click_restore_button()
    test_restore_by_mnemonic.choose_type_native()
    test_restore_by_mnemonic.conf_create_wallet()

@pytest.mark.usefixtures("driver")
@allure.feature("Restore wallet by idvalid mnemonic")
@pytest.mark.parametrize("data, expected_error", [
    ("", "Please insert all the words"),
    (Data.INVALID_MNEMONIC_DATA , "Please insert all the words")])
# Checking the negative options for creating a mnemonic
def test_invalid_restore_by_mnemonic(driver, data, expected_error):

    test_invalid_restore_by_mnemonic = CreateMnemonic(driver)

    test_invalid_restore_by_mnemonic.exec_id()
    test_invalid_restore_by_mnemonic.use_id()

    time.sleep(0.5)
    test_invalid_restore_by_mnemonic.enter_password(Data.PASS)
    test_invalid_restore_by_mnemonic.conf_password(Data.CONFPASS)
    test_invalid_restore_by_mnemonic.click_reg_button()
    test_invalid_restore_by_mnemonic.type_reg_mnemonic()
    test_invalid_restore_by_mnemonic.type_reg_restore_mnem(data)
    test_invalid_restore_by_mnemonic.click_restore_button()
    time.sleep(0.5)

    try:
        error_message = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "error"))
        )
        assert error_message.is_displayed(), "The error message is not displayed"
        assert error_message.text == expected_error, f"An error message was expected: '{expected_error}', but received: '{error_message.text}'"
    except Exception as e:
        pytest.fail(f"Message validation error: {e}")