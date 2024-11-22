import allure
import pytest
import time
from autotests.data import Data
from autotests.tests.wallet_tests.test_wallet_recovery_by_private_key import restore_by_private_key_proc, restore_zero_balance_wallet
from autotests.pages.wallet.wallet_mane_page import ManePage
from autotests.pages.wallet.wallet_settings_page import WalletSettings
from autotests.pages.wallet.wallet_nft_page import TransfersPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("driver")
@allure.feature("Valid sending transfers from the wallet")
def test_valid_sending_transfers(driver):

    mane_page = ManePage(driver)
    settings = WalletSettings(driver)
    bel_page = TransfersPage(driver)

    # Private key authentication
    ex_id, password = restore_by_private_key_proc(driver)

    settings.change_network(ex_id) # change network to Testnet
    
    mane_page.settings_page_btn()

    settings.change_type_legacy()
    
    first_check = bel_page.check_balance()
    
    mane_page.nft_page_btn()
    
    bel_page.bel_btn()
    bel_page.select_transfer()
    bel_page.send_btn()
    bel_page.address_input(Data.VALID_ADDRESS_FOR_CHECK)
    bel_page.select_amount()
    bel_page.send_btn()
    
    success_message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'toast ')]"))
    )
    assert success_message.is_displayed(), "Expected a success message, but it was not displayed."

    # Extract and validate success message text
    success_text = success_message.text
    allure.attach(f"Success message: {success_text}", name="Success Message", attachment_type=allure.attachment_type.TEXT)

    expected_success = "Successfully sended transfer(s)" 
    assert expected_success in success_text, (
        f"Expected success message '{expected_success}', but got '{success_text}'"
    )
    second_check = bel_page.check_balance()
    
    #  # Assert the balance has decreased
    # assert second_check < first_check, (
    #     f"Balance did not decrease after transfer. "
    #     f"Initial: {first_check}, After: {second_check}"
    # )
 
    
@pytest.mark.usefixtures("driver")
@allure.feature("Verification of sending an transfers with an incorrectly specified address")
def test_invalid_sending_transfers(driver):

    mane_page = ManePage(driver)
    settings = WalletSettings(driver)
    bel_page = TransfersPage(driver)

    # Private key authentication
    ex_id, password = restore_by_private_key_proc(driver)

    settings.change_network(ex_id) # change network to Testnet
    
    mane_page.settings_page_btn()

    settings.change_type_legacy()
    
    first_check = bel_page.check_balance()
    
    mane_page.nft_page_btn()
    
    bel_page.bel_btn()
    bel_page.select_transfer()
    bel_page.send_btn()
    bel_page.address_input(Data.NOT_VALID_ADDRESS)
    bel_page.select_amount()
    bel_page.send_btn()
    
    # Locate error message
    error_message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'toast ')]"))
    )
    assert error_message.is_displayed(), "Expected an error, but no error was displayed."

    # Extract and validate error message text
    error_text = error_message.text
    allure.attach(error_text, name="Error Message", attachment_type=allure.attachment_type.TEXT)


@pytest.mark.usefixtures("driver")
@allure.feature("Сheck of transfer sending from a wallet without balance")
def test_valid_sending_transfers_zero_wallet(driver):

    mane_page = ManePage(driver)
    settings = WalletSettings(driver)
    bel_page = TransfersPage(driver)

    # Private key authentication
    ex_id, password = restore_zero_balance_wallet(driver)

    settings.change_network(ex_id) # change network to Testnet
    
    first_check = bel_page.check_balance()
    
    mane_page.nft_page_btn()
    
    bel_page.bel_btn()
    bel_page.select_transfer()
    bel_page.send_btn()
    bel_page.address_input(Data.VALID_ADDRESS_FOR_CHECK)
    bel_page.select_amount()
    bel_page.send_btn()

    # Locate error message
    error_message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'toast ')]"))
    )
    assert error_message.is_displayed(), "Expected an error, but no error was displayed."

    # Extract and validate error message text
    error_text = error_message.text
    allure.attach(error_text, name="Error Message", attachment_type=allure.attachment_type.TEXT)