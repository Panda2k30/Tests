import time
import allure
import pytest
from AutoTests.pages.wallet.wallet_registration_page import CreateMnemonic
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

@pytest.mark.usefixtures("driver")
@allure.feature("Create valid wallet password")
@pytest.mark.parametrize("password, conf_password", [
    ("ItsA_ValidPassw0rd", "ItsA_ValidPassw0rd") ])

def test_create_valid_password(driver, password, conf_password):

    test_create_valid_password = CreateMnemonic(driver)

    test_create_valid_password.exec_id()
    test_create_valid_password.use_id()

    time.sleep(0.5)
    test_create_valid_password.enter_password(password) # Ввод пароля
    test_create_valid_password.conf_password(conf_password) # Подтверждение пароля
    test_create_valid_password.click_reg_button() # Жмем на кнопку продолжения

    try:
        dashboard_element = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "New mnemonic")))
        assert dashboard_element.is_displayed(), "Элемент на странице не отображается"
    except TimeoutException:
        pytest.fail("Время ожидания истекло")

@pytest.mark.usefixtures("driver")
@allure.feature("Create invalid wallet password")
@pytest.mark.parametrize("password, conf_password, expected_error", [
    ("a1234567", "7654321a", "Passwords dismatches"),
    ("", "a1234567", None),
    ("a1234567", "", None),
    ("", "", None),
])

def test_create_invalid_password(driver, password, conf_password, expected_error):
    test_create_invalid_password = CreateMnemonic(driver)

    test_create_invalid_password.exec_id()
    test_create_invalid_password.use_id()

    time.sleep(0.5)
    test_create_invalid_password.enter_password(password)
    test_create_invalid_password.conf_password(conf_password)
    test_create_invalid_password.click_reg_button()

    if password and conf_password:
        try:
            error_message = WebDriverWait(driver, 1.2).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "error"))
            )
            assert error_message.is_displayed(), "The error message is not displayed"
            assert error_message.text == expected_error, f"An error message was expected: '{expected_error}', but received: '{error_message.text}'"
        except TimeoutException:
            pytest.fail("Timeout expired: no error message found")
    else:
        error_displayed = len(driver.find_elements(By.CLASS_NAME, "error")) > 0
        assert not error_displayed, "The error message should not be displayed if one of the fields is empty"
