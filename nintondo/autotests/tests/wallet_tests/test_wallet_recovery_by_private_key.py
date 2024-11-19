import time
import allure
import pytest
from autotests.pages.wallet.wallet_registration_page import CreateMnemonic
from autotests.data import Data
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
    password = test_restore_by_private_key.enter_password() # Enter password
    test_restore_by_private_key.conf_password(password) # Confirm password
    test_restore_by_private_key.click_reg_button() # Press the continue button
    test_restore_by_private_key.type_reg_privacy_key() # Select private key recovery
    test_restore_by_private_key.restore_input(Data.KEY_MONEY_WALLET) # Enter private key
    test_restore_by_private_key.conf_create_wallet() # Confirm wallet creation
    test_restore_by_private_key.conf_recover_wallet()  # Confirm wallet creation

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[span='Receive']"))
    )

    assert element is not None, "Element with the specified class was not found."
    
    return ex_id, password

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
    password = test_restore_by_invalid_private_key.enter_password() # Enter password
    test_restore_by_invalid_private_key.conf_password(password) # Confirm password
    test_restore_by_invalid_private_key.click_reg_button()
    test_restore_by_invalid_private_key.type_reg_privacy_key()
    test_restore_by_invalid_private_key.restore_input(data)
    test_restore_by_invalid_private_key.conf_create_wallet()
    test_restore_by_invalid_private_key.conf_recover_wallet()

    try:
        error_message = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "error"))
        )
        assert error_message.is_displayed(), "Error message is not displayed"
        assert error_message.text == expected_error, f"An error message was expected: '{expected_error}', but received: '{error_message.text}'"
    except Exception as e:
        pytest.fail(f"Error during message validation: {e}")
      
# SETUPS

# Authorization function without launching an unnecessary web driver       
def restore_by_private_key_proc(driver):

    restore_by_private_key_proc = CreateMnemonic(driver)

    ex_id = restore_by_private_key_proc.exec_id()
    restore_by_private_key_proc.use_id()

    time.sleep(0.5)
    password = restore_by_private_key_proc.enter_password() # Enter password
    restore_by_private_key_proc.conf_password(password) # Confirm password
    restore_by_private_key_proc.click_reg_button() # Press the continue button
    restore_by_private_key_proc.type_reg_privacy_key() # Select private key recovery
    restore_by_private_key_proc.restore_input(Data.KEY_MONEY_WALLET) # Enter private key
    restore_by_private_key_proc.conf_create_wallet() # Confirm wallet creation
    restore_by_private_key_proc.conf_recover_wallet()  # Confirm wallet creation

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[span='Receive']"))
    )

    assert element is not None, "Element with the specified class was not found."
    
    return ex_id, password
 
# Zero balance wallet         
def restore_zero_balance_wallet (driver):

    restore_zero_balance_wallet = CreateMnemonic(driver)

    ex_id = restore_zero_balance_wallet.exec_id()
    restore_zero_balance_wallet.use_id()

    time.sleep(0.5)
    password = restore_zero_balance_wallet.enter_password() # Enter password
    restore_zero_balance_wallet.conf_password(password) # Confirm password
    restore_zero_balance_wallet.click_reg_button() # Press the continue button
    restore_zero_balance_wallet.type_reg_privacy_key() # Select private key recovery
    restore_zero_balance_wallet.restore_input(Data.ZERO_WALLET_FOR_CHECK) # Enter private key
    restore_zero_balance_wallet.conf_create_wallet() # Confirm wallet creation
    restore_zero_balance_wallet.conf_recover_wallet()  # Confirm wallet creation

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[span='Receive']"))
    )

    assert element is not None, "Element with the specified class was not found."
    
    return ex_id, password