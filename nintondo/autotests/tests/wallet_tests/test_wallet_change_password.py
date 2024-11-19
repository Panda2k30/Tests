import allure
import pytest
from autotests.tests.wallet_tests.test_wallet_recovery_by_private_key import restore_by_private_key_proc
from autotests.pages.wallet.wallet_mane_page import ManePage
from autotests.data import Data
from autotests.pages.wallet.wallet_settings_page import SettingsSecurity, ChangePassword
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

@pytest.mark.usefixtures("driver")
@allure.feature("Valid: Changing the password in the wallet")
def test_valid_changing_password(driver):
    
    ex_id, password = restore_by_private_key_proc(driver)
    
    mane_page = ManePage(driver)
    mane_page.settings_page_btn()
    
    security_page = SettingsSecurity(driver)
    security_page.security_page()
    
    change_password = ChangePassword(driver)

    change_password.change_password_page()
    change_password.old_password(password)
    new_password = change_password.new_password()
    change_password.conf_password(new_password)
    change_password.conf_btn()
    
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[text()='Welcome back']"))
    )

    assert element is not None, "Element with the specified class was not found."
    allure.attach("Verification complete. Password successfully changed", name="Verification Message", attachment_type=allure.attachment_type.TEXT)
    

@pytest.mark.usefixtures("driver")
@allure.feature("Test Design: Changing the password in the wallet")
@pytest.mark.parametrize("new_pass, conf_pass, expected_error", [
    ("", "", "error"),
    (Data.FIRST_LARGE_PASSWORD, "1nvalid", "error"),
    (Data.FIRST_LARGE_PASSWORD, Data.FIRST_LARGE_PASSWORD, "success"),
    (Data.SECOND_LARGE_PASSWORD, Data.SECOND_LARGE_PASSWORD, "success"),
    (Data.SET_LARGE_PASSWORD, Data.SET_LARGE_PASSWORD, "error"),
    ])
def test_changing_password(driver, new_pass, conf_pass, expected_error):
    
    ex_id, password = restore_by_private_key_proc(driver)
    
    mane_page = ManePage(driver)
    mane_page.settings_page_btn()
    
    security_page = SettingsSecurity(driver)
    security_page.security_page()
    
    change_password = ChangePassword(driver)

    change_password.change_password_page()
    change_password.old_password(password)
    change_password.test_password(new_pass)
    change_password.conf_password(conf_pass)
    change_password.conf_btn()
    
    
    time.sleep(0.3)
    if expected_error == "error":
        error_message = driver.find_element(By.XPATH, "//div[contains(@class, 'toast ')]")
        assert error_message.is_displayed(), "Expected an error, but no error was displayed."
        error_text = error_message.text
        allure.attach(error_text, name="Error Message", attachment_type=allure.attachment_type.TEXT)

    elif expected_error == "success":
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='Welcome back']"))
        )
        assert success_message is not None, "Element with the text 'Welcome back' was not found."
        allure.attach("Success: Welcome back message displayed", name="Success Message", attachment_type=allure.attachment_type.TEXT)