import time
import allure
import pytest
from Nintondo.AutoTests.Pages.Registration_page import CreateMnemonic
from Nintondo.AutoTests.Data import Data
from Nintondo.AutoTests.Pages.Mane_page import ManePage
from .test_registration import test_restore_by_private_key

@allure.feature("Send money and verify balance")
@pytest.mark.usefixtures("driver")
def test_sendmoney(driver):

    test_restore_by_private_key(driver) # Добавляем кошелек через приватный ключ
    test_sendmoney = ManePage(driver)
    test_sendmoney.get_balance()
    test_sendmoney.change_network()

    test_sendmoney.get_balance()