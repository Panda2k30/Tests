import allure
import pytest
import time
from autotests.data import Data
from autotests.tests.wallet_tests.test_wallet_recovery_by_private_key import restore_by_private_key_proc, restore_zero_balance_wallet
from autotests.pages.wallet.wallet_registration_page import CreateMnemonic
from autotests.pages.wallet.wallet_mane_page import ManePage
from autotests.pages.wallet.wallet_nft_page import SendInscription
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


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

    allure.attach("Data collation ...", name="Data Collation", attachment_type=allure.attachment_type.TEXT)

    # compare all the data
    assert account_address == from_address_tabl, f"Address mismatch: {account_address} != {from_address_tabl}"
    assert valid_address == to_address_tabl, f"Address mismatch: {valid_address} != {to_address_tabl}"
    assert id_card == id_tabl, f"ID mismatch: {id_card} != {id_tabl}"

    allure.attach("Successfully!", name="Success", attachment_type=allure.attachment_type.TEXT)

    nft_page.confirm_btn()
    allure.attach("Sent the transcript to a different address!", name="Transaction Sent", attachment_type=allure.attachment_type.TEXT)
    
    expected_success_message = "Success"
    try:
        success_message = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//h3[text()='Success']")))
        
        assert success_message.is_displayed(), "The success message is not displayed"
        assert success_message.text == expected_success_message, \
            f"Expected success message: '{expected_success_message}', but got: '{success_message.text}'"
    except Exception as e:
        pytest.fail(f"Error when checking success message after publication: {e}")

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

    allure.attach("Check that the TXIDs are the same...", name="TXID Check", attachment_type=allure.attachment_type.TEXT)
    
    # Check that the TXIDs are the same
    assert are_txids_same(second_wallet_txid, first_wallet_txid), (
        f"TXID has changed! Old value: {first_wallet_txid}, "
        f"New value: {second_wallet_txid}"
    )
    allure.attach("Successfully!", name="Success", attachment_type=allure.attachment_type.TEXT)


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
    allure.attach(f"Error message: {error_text}", name="Error Message", attachment_type=allure.attachment_type.TEXT)
    
    
@pytest.mark.usefixtures("driver")
@allure.feature("Verification of sending inscription from a wallet without a balance")
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
    
    # time.sleep(0.3)
    error_message = WebDriverWait(driver, 5).until(
         EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'toast ')]")))
    assert error_message.is_displayed(), "Expected an error, but no error was displayed."

    allure.attach(f"Error message: {error_message.text}", name="Error Message", attachment_type=allure.attachment_type.TEXT)
