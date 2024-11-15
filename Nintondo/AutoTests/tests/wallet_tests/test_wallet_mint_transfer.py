import allure
import pytest
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from AutoTests.data import Data
from AutoTests.tests.wallet_tests.test_wallet_recovery_by_private_key import restore_by_private_key_proc, restore_zero_balance_wallet
from AutoTests.pages.wallet.wallet_registration_page import CreateMnemonic
from AutoTests.pages.wallet.wallet_mane_page import ManePage
from AutoTests.pages.wallet.wallet_nft_page import SendInscription
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("driver")
@allure.feature("Valid minting transfers from the wallet")
def test_valid_minting_transfers(driver):

    # Private key authentication
    ex_id, password = restore_by_private_key_proc(driver)

    change_network = ManePage(driver)

    change_network.change_network(ex_id) # change network to Testnet
    change_network.get_balance()

    account_address = change_network.account_address_btn() # get a wallet address
    change_network.nft_page_btn()
    
    