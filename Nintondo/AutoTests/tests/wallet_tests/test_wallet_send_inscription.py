import time
import allure
import pytest
from Nintondo.AutoTests.data import Data
from Nintondo.AutoTests.conftest import driver
from Nintondo.AutoTests.tests.wallet_tests.test_wallet_recovery_by_private_key import test_restore_by_private_key
from Nintondo.AutoTests.pages.wallet.wallet_mane_page import ManePage
from Nintondo.AutoTests.pages.wallet.wallet_nft_page import NFTPage

@pytest.mark.usefixtures("driver")
@allure.feature("Valid sending inscriptions from the wallet")
def test_valid_sending_inscriptions(driver):

    ex_id = test_restore_by_private_key(driver)

    change_network = ManePage(driver)
    time.sleep(0.2)
    change_network.change_network(ex_id)
    time.sleep(0.5)
    change_network.get_balance()

    account_address = change_network.account_address_btn()
    change_network.nft_page_btn()

    nft_page = NFTPage(driver)

    nft_page.select_inscription()
    id_card = nft_page.id_card()
    nft_page.send_btn()
    valid_address = nft_page.enter_address(Data.VALID_RECEIVE_ADDRESS)
    nft_page.continue_btn()
    to_address_tabl = nft_page.to_address_tabl()
    from_address_tabl = nft_page.from_address_tabl()
    id_tabl = nft_page.id_tabl()
    print("Data collation")
    assert account_address == from_address_tabl, f"Address mismatch: {account_address} != {from_address_tabl}"
    assert valid_address == to_address_tabl, f"Address mismatch: {valid_address} != {to_address_tabl}"
    assert id_card == id_tabl, f"ID mismatch: {id_card} != {id_tabl}"
    print("Successfully")