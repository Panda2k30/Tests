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
@allure.feature("Valid sending inscriptions from the wallet")
def test_valid_sending_inscriptions(driver):

    def are_txids_same(txid1, txid2):
        return txid1 == txid2

    # Private key authentication
    ex_id, password = restore_by_private_key_proc(driver)

    change_network = ManePage(driver)

    change_network.change_network(ex_id) # change network to Testnet
    change_network.get_balance()

    account_address = change_network.account_address_btn() # get a wallet address
    change_network.nft_page_btn()

    nft_page = SendInscription(driver)

    nft_page.select_inscription()
    id_card = nft_page.return_id_card() # get the inscription id

    nft_page.send_btn()

    valid_address = nft_page.enter_address(Data.VALID_ADDRESS_FOR_CHECK) # get the recipient's address
    nft_page.continue_btn()

    # output all data
    to_address_tabl = nft_page.return_to_address_tabl()
    from_address_tabl = nft_page.return_from_address_tabl()
    id_tabl = nft_page.return_id_tabl()

    print("\nData collation ...")

    # compare all the data
    assert account_address == from_address_tabl, f"Address mismatch: {account_address} != {from_address_tabl}"
    assert valid_address == to_address_tabl, f"Address mismatch: {valid_address} != {to_address_tabl}"
    assert id_card == id_tabl, f"ID mismatch: {id_card} != {id_tabl}"

    print("\nSuccessfully !")

    nft_page.confirm_btn()
    print("\nSent the transcript to a different address !\n")

    nft_page.back_btn()

    first_wallet_txid = change_network.verify_transaction()
    change_network.wallet_page_btn()
    change_network.add_wallet_btn()

    restore_by_private_key = CreateMnemonic(driver)

    restore_by_private_key.type_reg_privacy_key()
    restore_by_private_key.restore_input(Data.KEY_WALLET_FOR_CHECK)
    restore_by_private_key.conf_create_wallet()
    restore_by_private_key.conf_recover_wallet()

    change_network.trans_cont()

    second_wallet_txid = change_network.verify_transaction()

    print("\nCheck that the TXIDs are the same ...")
    # Check that the TXIDs are the same
    assert are_txids_same(second_wallet_txid, first_wallet_txid), (
        f"TXID has changed! Old value: {first_wallet_txid}, "
        f"New value: {second_wallet_txid}"
    )
    print("\nSuccessfully !")


# incorrect address
@pytest.mark.usefixtures("driver")
@allure.feature("Verification of sending an inscription with an incorrectly specified address")
def test_invalid_sending_inscriptions(driver):

    # Private key authentication
    ex_id, password = restore_by_private_key_proc(driver)

    change_network = ManePage(driver)

    change_network.change_network(ex_id) # change network to Testnet
    change_network.get_balance()

    change_network.account_address_btn()
    change_network.nft_page_btn()

    nft_page = SendInscription(driver)

    nft_page.select_inscription()
    nft_page.return_id_card()

    nft_page.send_btn()

    nft_page.enter_address(Data.NOT_VALID_ADDRESS)
    nft_page.continue_btn()
    
    time.sleep(0.3)
    error_message = driver.find_element(By.XPATH, "//div[contains(@class, 'toast ')]")
    assert error_message.is_displayed(), "Expected an error, but no error was displayed."
    error_text = error_message.text
    print(f"\nError message: {error_text}")
    
    
# insufficient balance
@pytest.mark.usefixtures("driver")
@allure.feature("Verification of sending an inscription with an incorrectly specified address")
def test_valid_sending_inscriptions_zero_wallet(driver):

    # Private key authentication
    ex_id, password = restore_zero_balance_wallet(driver)

    change_network = ManePage(driver)

    change_network.change_network(ex_id) # change network to Testnet
    change_network.get_balance()

    change_network.account_address_btn()
    change_network.nft_page_btn()

    nft_page = SendInscription(driver)

    nft_page.select_inscription()
    nft_page.return_id_card()

    nft_page.send_btn()

    nft_page.enter_address(Data.VALID_ADDRESS_FOR_CHECK)
    nft_page.continue_btn()
    
    time.sleep(0.3)
    error_message = driver.find_element(By.XPATH, "//div[contains(@class, 'toast ')]")
    assert error_message.is_displayed(), "Expected an error, but no error was displayed."
    
    error_text = error_message.text
    
    print(f"\nError message: {error_text}")
    
    expected_error = "Balance not enough to pay network fee." 
    assert expected_error in error_text, f"Expected error message '{expected_error}', but got '{error_text}'"