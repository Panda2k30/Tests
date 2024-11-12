import time
import allure
import pytest
from Nintondo.AutoTests.pages.wallet.wallet_registration_page import CreateMnemonic
from Nintondo.AutoTests.data import Data
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("driver")
@allure.feature("Restore wallet by private key")

def test_restore_by_private_key(driver):

    test_restore_by_private_key = CreateMnemonic(driver)

    ex_id = test_restore_by_private_key.exec_id()
    test_restore_by_private_key.use_id()

    time.sleep(0.5)
    test_restore_by_private_key.enter_password(Data.PASS) # Enter password
    test_restore_by_private_key.conf_password(Data.CONFPASS) # Confirm password
    test_restore_by_private_key.click_reg_button() # Press the continue button
    test_restore_by_private_key.type_reg_privacy_key() # Select private key recovery
    test_restore_by_private_key.restore_input(Data.KEY_MONEY_WALLET) # Enter private key
    test_restore_by_private_key.conf_create_wallet() # Confirm wallet creation
    print("// Choose wallet type: Native, by default //")
    test_restore_by_private_key.conf_recover_wallet()  # Confirm wallet creation

    return ex_id

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
        assert error_message.is_displayed(), "Error message is not displayed"
        assert error_message.text == expected_error, f"An error message was expected: '{expected_error}', but received: '{error_message.text}'"
    except Exception as e:
        pytest.fail(f"Error during message validation: {e}")