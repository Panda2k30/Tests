import allure
import pytest
import time
from autotests.tests.wallet_tests.test_wallet_recovery_by_private_key import restore_by_private_key_proc, restore_zero_balance_wallet
from autotests.pages.wallet.wallet_mane_page import ManePage
from autotests.pages.wallet.wallet_settings_page import WalletSettings
from autotests.pages.wallet.wallet_nft_page import TransfersPage
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("driver")
@allure.feature("Valid minting transfers from the wallet")
def test_valid_minting_transfers(driver):

    mane_page = ManePage(driver)
    settings = WalletSettings(driver)
    bel_page = TransfersPage(driver)

    # Private key authentication
    ex_id, password = restore_by_private_key_proc(driver)

    settings.change_network(ex_id) # change network to Testnet
    
    mane_page.settings_page_btn()

    settings.change_type_legacy()
    
    first_check = bel_page.check_transfer_balance()
    
    mane_page.nft_page_btn()
    
    bel_page.bel_btn()
    bel_page.select_transfer()
    bel_page.mint_btn()
    bel_page.amount(2)
    bel_page.inscribe_btn()
    
    # Check for success message
    time.sleep(0.6)
    
    # Locate success message
    success_message = driver.find_element(By.XPATH, "//div[contains(@class, 'toast ')]")
    assert success_message.is_displayed(), "Expected a success message, but it was not displayed."

    # Extract and validate success message text
    success_text = success_message.text
    allure.attach(success_text, name="Success Message", attachment_type=allure.attachment_type.TEXT)

    expected_success = "Transfer inscribed successfully" 
    assert expected_success in success_text, (
        f"Expected success message '{expected_success}', but got '{success_text}'"
    )
    
    second_check = bel_page.check_transfer_balance()
    
    # assert second_check == first_check + 2, (
    #     f"Transferable balance didn't increase correctly. "
    #     f"Initial balance: {first_check}, "
    #     f"New balance: {second_check}, "
    #     f"Amount added: 2"
    # )

     
@pytest.mark.usefixtures("driver")
@allure.feature("Verification of transfer mint from a wallet without balance")
def test_mint_transfer_zero_wallet(driver):

    mane_page = ManePage(driver)
    settings = WalletSettings(driver)
    bel_page = TransfersPage(driver)

    # Private key authentication
    ex_id, password = restore_zero_balance_wallet(driver)

    settings.change_network(ex_id) # change network to Testnet
    
    first_check = bel_page.check_transfer_balance()
    
    mane_page.nft_page_btn()
    
    bel_page.bel_btn()
    bel_page.select_transfer()
    bel_page.mint_btn()
    bel_page.amount(2)
    bel_page.inscribe_btn()
    
    time.sleep(0.4)
    # Locate error message
    error_message = driver.find_element(By.XPATH, "//div[contains(@class, 'toast ')]")
    assert error_message.is_displayed(), "Expected an error, but no error was displayed."

    # Extract and validate error message text
    error_text = error_message.text
    allure.attach(error_text, name="Error Message", attachment_type=allure.attachment_type.TEXT)

    expected_error = "Insufficient balance. Non-Inscription balance" 
    assert expected_error in error_text, f"Expected error message '{expected_error}', but got '{error_text}'"

    # Second check
    second_check = bel_page.check_transfer_balance()