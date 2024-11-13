import allure
import pytest
from AutoTests.tests.wallet_tests.test_wallet_recovery_by_private_key import restore_by_private_key_proc
from AutoTests.pages.wallet.wallet_mane_page import ManePage
from AutoTests.pages.wallet.wallet_settings_page import SettingsSecurity, ChangePassword
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

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
    print("\nVerification complete. Password successfully changed")