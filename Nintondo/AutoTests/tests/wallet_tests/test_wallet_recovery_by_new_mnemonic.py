import time
import allure
import pytest
from AutoTests.pages.wallet.wallet_registration_page import CreateMnemonic
from AutoTests.data import Data
from AutoTests.pages.wallet.wallet_registration_page import LoginPageSelectors
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("driver")
@allure.feature("Valid Create wallet with new Mnemonic")

def test_valid_create_mnemonic(driver):

    test_create_mnemonic = CreateMnemonic(driver)

    test_create_mnemonic.exec_id()
    test_create_mnemonic.use_id()
    time.sleep(0.5)
    test_create_mnemonic.enter_password(Data.PASS) # Enter password
    test_create_mnemonic.conf_password(Data.CONFPASS) # Confirm password
    test_create_mnemonic.click_reg_button() # Hit the continue button
    test_create_mnemonic.type_reg_new_mnem() # Select authorization type: New mnemonic
    # test_create_mnemonic.copy_mnem() # Копируем фразы
    # test_create_mnemonic.paste_mnen() # Выводим фразы
    test_create_mnemonic.conf_save() # Confirm that the mnemonic has been saved
    test_create_mnemonic.conf_create_wallet() # Confirm wallet creation
    print("// Choose wallet type: Native, by default //")
    test_create_mnemonic.conf_create_wallet() # Confirm wallet creation

@pytest.mark.usefixtures("driver")
@allure.feature("Invalid Create wallet with new Mnemonic")

def test_invalid_create_mnemonic(driver):

    test_invalid_create_mnemonic = CreateMnemonic(driver)

    test_invalid_create_mnemonic.exec_id()
    test_invalid_create_mnemonic.use_id()
    time.sleep(0.5)
    test_invalid_create_mnemonic.enter_password(Data.PASS)
    test_invalid_create_mnemonic.conf_password(Data.CONFPASS)
    test_invalid_create_mnemonic.click_reg_button()
    test_invalid_create_mnemonic.type_reg_new_mnem()

    createbtn_mnemonic = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(LoginPageSelectors.CREATE_BUTTON)
    )
    is_disabled_class = "disabled:cursor-not-allowed" in createbtn_mnemonic.get_attribute("class")

    assert is_disabled_class, "The button was expected to be inactive, but it is available."
    print("- The button is indeed inactive and has class disabled:cursor-not-allowed") 