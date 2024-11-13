import time
import allure
import pytest
from AutoTests.data import Data
from AutoTests.tests.wallet_tests.test_wallet_recovery_by_private_key import restore_by_private_key_proc
from AutoTests.pages.wallet.wallet_registration_page import CreateMnemonic
from AutoTests.pages.wallet.wallet_mane_page import ManePage

# Check the functionality of the extension when creating a large number of wallets
@pytest.mark.scripts("driver")
@allure.feature("Add a large number of wallets")

def test_add_wallets(driver):
    
    restore_by_private_key_proc(driver)
    
    manepage = ManePage(driver)
    add_by_private_key = CreateMnemonic(driver)
    
    for _ in range(500): 
        manepage.wallet_page_btn()
        manepage.add_wallet_btn()

        add_by_private_key.type_reg_privacy_key()
        add_by_private_key.restore_input(Data.KEY_WALLET_FOR_CHECK)
        add_by_private_key.conf_create_wallet()
        add_by_private_key.choose_type_legacy()
        add_by_private_key.conf_recover_wallet()
    