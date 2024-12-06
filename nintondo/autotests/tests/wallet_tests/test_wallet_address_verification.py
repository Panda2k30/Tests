import allure
import pytest
from autotests.conftest import driver
from autotests.tests.wallet_tests.test_wallet_recovery_by_private_key import restore_by_private_key_proc
from autotests.pages.wallet.wallet_mane_page import ManePage
from autotests.pages.wallet.wallet_receive_page import ReceivePage
import os

@pytest.mark.usefixtures("driver")
@allure.feature("wallet_tests address verification")

def test_wallet_address_verification(driver):

    ex_id, password = restore_by_private_key_proc(driver)

    test_wallet_address_verification = ManePage(driver)

    test_wallet_address_verification.get_balance()
    test_wallet_address_verification.change_network(ex_id)
    test_wallet_address_verification.receive_page_btn()

    check_address = ReceivePage(driver)

    received_address = check_address.receive_address_btn()
    received_address_text = check_address.receive_address_text()

    screenshot_folder = 'screenshots'
    screenshot_file_path = os.path.join(screenshot_folder, 'screenshot-address.png')
    driver.get_screenshot_as_file(screenshot_file_path)

    with open(screenshot_file_path, 'rb') as screenshot_file:
        allure.attach(screenshot_file.read(), name="Screenshot of the Address Page", attachment_type=allure.attachment_type.PNG) 
    
    test_wallet_address_verification.back_btn()
    account_address = test_wallet_address_verification.account_address_btn()

    assert received_address == account_address, f"Error: addresses do not match! Received address: '{received_address}', Expected address: '{account_address}'"
    assert received_address_text == account_address, f"Error: addresses do not match! Received address text: '{received_address_text}', Expected address: '{account_address}'"
