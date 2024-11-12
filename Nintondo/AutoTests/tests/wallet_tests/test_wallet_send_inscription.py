import time
import allure
import pytest
from Nintondo.AutoTests.data import Data
from Nintondo.AutoTests.conftest import driver
from Nintondo.AutoTests.pages.wallet.wallet_registration_page import CreateMnemonic
from Nintondo.AutoTests.pages.wallet.wallet_mane_page import ManePage
from Nintondo.AutoTests.pages.wallet.wallet_send_page import SendPage

@pytest.mark.usefixtures("driver")
@allure.feature("Valid sending inscriptions from the wallet")
def test_check_balance(driver):

    def are_txids_different(txid1, txid2):
        # Check if TXIDs differ by at least one character
        return any(char1 != char2 for char1, char2 in zip(txid1, txid2)) or len(txid1) != len(txid2)

    restore_by_private_key = CreateMnemonic(driver)
    sendmoney = SendPage(driver)
    change_network = ManePage(driver)

    ex_id = restore_by_private_key.exec_id()
    restore_by_private_key.use_id()

    time.sleep(0.5)

    # Ввод пароля и восстановление кошелька
    restore_by_private_key.enter_password(Data.PASS)
    restore_by_private_key.conf_password(Data.CONFPASS)
    restore_by_private_key.click_reg_button()

    restore_by_private_key.type_reg_privacy_key()
    restore_by_private_key.restore_input(Data.KEY_MONEY_WALLET)
    restore_by_private_key.conf_create_wallet()
    print("Choose wallet type: Native, by default")
    restore_by_private_key.conf_recover_wallet()

    time.sleep(0.5)
    change_network.get_balance()
    change_network.change_network(ex_id)
    time.sleep(0.5)
    change_network.get_balance()

    old_transaction_verify = change_network.verify_transaction()

    change_network.send_page_btn()

    sendmoney.enter_address(Data.VALID_RECEIVE_ADDRESS)
    sendmoney.enter_amount(valid_amount=0.1)
    sendmoney.include_fee()
    sendmoney.save_address()
    sendmoney.cont_send_money()
    sendmoney.conf_send_money()
    sendmoney.back_to_home()
    time.sleep(0.5)

    change_network.get_balance()
    new_transaction_verify = change_network.verify_transaction()

    assert are_txids_different(new_transaction_verify, old_transaction_verify), (
        f"TXID has not changed! Old value: {old_transaction_verify}, "
        f"New meaning: {new_transaction_verify}"
    )
    time.sleep(0.2)