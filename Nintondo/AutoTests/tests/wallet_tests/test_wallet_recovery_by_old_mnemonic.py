import time
import allure
import pytest
from AutoTests.pages.wallet.wallet_registration_page import CreateMnemonic
from AutoTests.data import Data
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("driver")
@allure.feature("Restore wallet by valid mnemonic")

def test_restore_by_mnemonic(driver):

    test_restore_by_mnemonic = CreateMnemonic(driver)

    test_restore_by_mnemonic.exec_id()
    test_restore_by_mnemonic.use_id()

    time.sleep(0.5)
    password = test_restore_by_mnemonic.enter_password() # Enter password
    test_restore_by_mnemonic.conf_password(password) # Confirm password
    test_restore_by_mnemonic.click_reg_button()  # Press the continue button
    test_restore_by_mnemonic.type_reg_mnemonic()  # Choose recovery through mnemonics
    test_restore_by_mnemonic.type_reg_restore_mnem(Data.VALID_MNEMONIC_DATA)  # Inserting mnemonics
    test_restore_by_mnemonic.click_restore_button()  # Press the continue button
    test_restore_by_mnemonic.choose_type_native()   # Select: Native Segwit
    test_restore_by_mnemonic.conf_create_wallet() # Confirm wallet creation

@pytest.mark.usefixtures("driver")
@allure.feature("Restore wallet by idvalid mnemonic")
@pytest.mark.parametrize("data, expected_error", [
    ("", "Please insert all the words"),
    (Data.INVALID_MNEMONIC_DATA , "Please insert all the words")])

def test_invalid_restore_by_mnemonic(driver, data, expected_error):

    test_invalid_restore_by_mnemonic = CreateMnemonic(driver)

    test_invalid_restore_by_mnemonic.exec_id()
    test_invalid_restore_by_mnemonic.use_id()

    time.sleep(0.5)
    password = test_invalid_restore_by_mnemonic.enter_password() # Enter password
    test_invalid_restore_by_mnemonic.conf_password(password) # Confirm password
    test_invalid_restore_by_mnemonic.click_reg_button()  # Press the continue button
    test_invalid_restore_by_mnemonic.type_reg_mnemonic()  # Choose recovery through mnemonics
    test_invalid_restore_by_mnemonic.type_reg_restore_mnem(data)  # Inserting mnemonics
    test_invalid_restore_by_mnemonic.click_restore_button() # Confirm wallet creation
    time.sleep(0.5)

    try:
        # Expect the error message to become visible
        error_message = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "error"))
        )
        assert error_message.is_displayed(), "The error message is not displayed"
        assert error_message.text == expected_error, f"An error message was expected: '{expected_error}', but received: '{error_message.text}'"
    except Exception as e:
        pytest.fail(f"Message validation error: {e}")