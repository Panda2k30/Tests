import time
import allure
import pytest
from autotests.data import Data
from autotests.conftest import driver
from autotests.tests.wallet_tests.test_wallet_recovery_by_private_key import restore_by_private_key_proc
from autotests.pages.wallet.wallet_mane_page import ManePage
from autotests.pages.wallet.wallet_send_page import SendPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("driver")
@allure.feature("Send money and verify balance")
def test_valid_sendmoney(driver):

    # Function to check for differences in TXID
    def are_txids_different(txid1, txid2):
        return any(char1 != char2 for char1, char2 in zip(txid1, txid2)) or len(txid1) != len(txid2)

    ex_id, password = restore_by_private_key_proc(driver)

    change_network = ManePage(driver)

    change_network.change_network(ex_id)
    change_network.get_balance()

    old_transaction_verify = change_network.verify_transaction()

    change_network.send_page_btn()

    # Sending funds
    sendmoney = SendPage(driver)

    sendmoney.enter_address(Data.VALID_ADDRESS_FOR_CHECK)
    sendmoney.enter_amount(valid_amount=0.1)
    sendmoney.include_fee()
    sendmoney.save_address()
    sendmoney.cont_send_money()
    sendmoney.conf_send_money()
    sendmoney.back_to_home()
    time.sleep(2)

    # Receive new balance and TXID
    change_network.get_balance()
    new_transaction_verify = change_network.verify_transaction()

    # Check that the TXID has changed
    assert are_txids_different(new_transaction_verify, old_transaction_verify), (
        f"TXID has not changed! Old value: {old_transaction_verify}, "
        f"New meaning: {new_transaction_verify}"
    )
    time.sleep(0.2)

@pytest.mark.usefixtures("driver")
@allure.feature("Sending money with an invalid balance")
@pytest.mark.parametrize("amount, blank, expected_error", [
    ("555555555", f"{Data.VALID_ADDRESS_FOR_CHECK}", "There's not enough money in your account"),
    ("", f"{Data.VALID_ADDRESS_FOR_CHECK}", "Minimum amount is 0.00000001 BEL"),
    ("0.1", "", "Invalid receiver's address"),
    ("", "", "Invalid receiver's address"),
    ("", f"{Data.NOT_VALID_ADDRESS}", "Invalid receiver's address"),
    ("0.00000001", f"{Data.VALID_ADDRESS_FOR_CHECK}", "Fee exceeds amount")
    ])

def test_invalid_sendmoney(driver, amount, blank, expected_error):

    ex_id, password = restore_by_private_key_proc(driver)

    change_network = ManePage(driver)

    change_network.change_network(ex_id)
    change_network.get_balance()
    change_network.send_page_btn()

    send_invalid_amount = SendPage(driver)

    send_invalid_amount.enter_address(blank)
    send_invalid_amount.enter_amount(amount)
    send_invalid_amount.include_fee()
    send_invalid_amount.cont_send_money()

    try:
        error_message = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "error"))
        )
        assert error_message.is_displayed(), "The error message is not displayed"
        assert error_message.text == expected_error, f"An error message was expected: '{expected_error}', but received: '{error_message.text}'"
    except Exception as e:
        pytest.fail(f"Error during message validation: {e}")