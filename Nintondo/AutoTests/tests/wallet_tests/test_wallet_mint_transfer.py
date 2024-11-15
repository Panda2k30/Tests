import allure
import pytest
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from AutoTests.data import Data
from AutoTests.tests.wallet_tests.test_wallet_recovery_by_private_key import restore_by_private_key_proc, restore_zero_balance_wallet
from AutoTests.pages.wallet.wallet_mane_page import ManePage
from AutoTests.pages.wallet.wallet_settings_page import WalletSettings
from AutoTests.pages.wallet.wallet_nft_page import TransfersPage
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
    
    first_check = bel_page.check_balance()
    
    mane_page.nft_page_btn()
    
    bel_page.bel_btn()
    bel_page.select_transfer()
    bel_page.mint_btn()
    bel_page.check_balance()
    bel_page.amount(2)
    bel_page.inscribe_btn()
    
    second_check = bel_page.check_balance()
    

    # assert second_check == first_check + 2, (
    #     f"Transferable balance didn't increase correctly. "
    #     f"Initial balance: {first_check}, "
    #     f"New balance: {second_check}, "
    #     f"Amount added: 2"
    # )
    
    
    
        